from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import AnswerForm, AnswerForm2, TestForm, QuestionForm
from django.contrib import messages
from django.http import Http404, HttpResponse
from django.utils.timezone import datetime
from django.db.models import Q
import math
import random







def login_required_decorator(func):
    return login_required(func,login_url='login')





def index(request):
    tests = Test.objects.all()
    if request.method == "GET":
        query = request.GET.get('q', "")
        tests = Test.objects.filter(Q(title__icontains=query))
    return render(request, "index.html", {'tests':tests})

@login_required_decorator
def my_tests(request):
    tests = Test.objects.filter(author=request.user)
    return render(request, "my_tests.html", {'tests':tests})

@login_required_decorator
def create_test(request):
    form = TestForm()
    if request.method == "POST":
        form = TestForm(data=request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.author = request.user
            form.save(commit=True)
            return redirect("index")
        else:
            return render(request, "create_test.html", {"form":form})
    return render(request, "create_test.html", {"form":form})

@login_required_decorator
def create_question(request, test_id):
    test = Test.objects.get(id=test_id)
    if request.method == "POST":
        qv=request.POST['question']
        question_name=Question.objects.filter(test=test, question=qv)
        if question_name.exists():
            messages.error(request,"Bu savolni testga qo'shgansiz")
            return redirect("create_question", test_id=test_id)
        else:
            form = QuestionForm(data=request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.test = test
                form.save(commit=True)
                messages.success(request, "Savol qo'shildi")
                request.session["question_id"]=question.id
                return redirect("create_answer", question.id)
            else:
                return render(request, "create_question.html", {'form':form, "test":test})
    else:
        form = QuestionForm()
        return render(request, "create_question.html", {'form':form, "test":test})



@login_required_decorator
def create_answer(request, question_id):
    question = Question.objects.get(id=question_id)
    form = AnswerForm2()

    if request.method == "POST":
        answer=request.POST['answer']
        answer_name=Answer.objects.filter(question=question, answer=answer)
        if answer_name.exists():
            messages.error(request,"Bu variantni savolga qo'shgansiz")
            return redirect("create_answer",question_id)
        else:
            add_again = request.POST.get("add-again")
            form = AnswerForm2(data=request.POST)
            if form.is_valid():
                answer = form.save(commit=False)
                answer.question = question
                form.save(commit=True)
                messages.info(request, "Variant qo'shildi")
                if add_again == "on":
                    return redirect("create_answer", question_id)
                else:
                    return redirect("detail_test",question.test_id)
    
            else:
                return render(request, "create_answer.html", {'form':form, "test":test})
    else:
        return render(request, "create_answer.html", {'form':form, "question":question})









@login_required_decorator
def update_test(request, test_id):
    test = Test.objects.get(id=test_id)
    user = request.user
    if user == test.author:
        form = TestForm(instance=test)
        if request.method == "POST":
            form = TestForm(instance=test, data=request.POST,)
            if form.is_valid():
                form.save()
                messages.success(request,"Test yangilandi")
                return redirect("my_tests")
    
            else:
                return render(request, "update_test.html", {"form":form, 'test':test})
        return render(request, "update_test.html", {"form":form, 'test':test})
    else:
        messages.error(request, "Bu test sizga tegishli emas!")
        return redirect('index')


@login_required_decorator
def detail_test(request, test_id):
    test = Test.objects.get(id=test_id)
    questions = Question.objects.filter(test=test)
    answ={}
    for q in questions:
        true_answers=Answer.objects.filter(question=q,is_true=True)
        for i in true_answers:
            answ[q]=i.answer

   
    
    return render(request, "detail_test.html", {"test":test, "questions":questions,'true_answers':answ})

@login_required_decorator
def delete_question(request,test_id, question_id):
    question = Question.objects.get(id=question_id)
    question.delete()
    messages.success(request,"Savol o'chirildi")
    return redirect("detail_test",test_id)





@login_required_decorator
def delete_answer(request,question_id,answer_id):
    answer = Answer.objects.get(id=answer_id)
    answer.delete()
    messages.success(request,"Variant o'chirildi")
    return redirect("update_question",question_id)





@login_required_decorator
def update_question(request, question_id):
    question = Question.objects.get(id=question_id)
    answers=Answer.objects.filter(question=question)

    user = request.user
    author = question.test.author

    if user == author:
        
        form = QuestionForm(instance=question,prefix=f"question-{question.id}")
        answers_forms=[]
        for i in answers:
            formm = AnswerForm(instance=i,prefix=f'form-{i.id}')
            answers_forms.append(formm)
        
        if request.method == "POST":
            q_form = QuestionForm(instance=question, data=request.POST,prefix=f"question-{question.id}")

            main_status=True
            if q_form.is_valid():
                q_form.save()
                main_status*=True
            else:
                main_status*=False
            for i in answers:
                frm=AnswerForm(instance=i, data=request.POST,prefix=f'form-{i.id}')
                if frm.is_valid():
                    frm.save()
                    main_status*=True
                else:
                    main_status*=False
            if main_status:
                messages.success(request, "Savol muvaffaqiyatli yangilandi")
                return redirect("detail_test", question.test.id)  
            else:
                return render(request, "update_question.html", {"form":form, "question":question})
        else:   
            return render(request, "update_question.html", {"form":form, "question":question,"answer_forms":answers_forms})
    else:
        messages.error(request, "Bu savol sizga tegishli emas!")
        return redirect('index')





@login_required_decorator
def ready_to_test(request, test_id):
    test = Test.objects.get(id=test_id)
    attemps = CheckTest.objects.filter(test=test, user=request.user).count()
    if str(test.start_date) > str(datetime.now()):
        return HttpResponse("Test boshlanish vaqti kelmagan")
    elif str(test.end_date) < str(datetime.now()):
        return HttpResponse("Test vaqti o'tib ketgan.")
    elif attemps >= test.maximum_attemps:
        return HttpResponse("Urunishlar tugadi")
    else:
        return render(request, "ready_to_test.html", {'test':test})
    


def test(request, test_id):
    test = Test.objects.get(id=test_id)
    qv_count=test.question_count
    qvv= questions = Question.objects.filter(test=test)[:qv_count]
    
    if qv_count>questions.count():
        qv_count=questions.count()

    if test.is_random:
        qvv = random.sample(list(questions), k=qv_count)


    qv_dict={}
    for q in qvv:
        answers=Answer.objects.filter(question=q)
        qv_dict[q]=answers
    if request.user.is_authenticated:
        attemps = CheckTest.objects.filter(test=test, user=request.user).count()
        if attemps >= test.maximum_attemps:
            return HttpResponse("Urunishlar tugadi")
    if str(test.start_date) > str(datetime.now()):
        return HttpResponse("Testni boshlanish vaqti kelmagan.")
    elif str(test.end_date) < str(datetime.now()):
        return HttpResponse("Testni  vaqti o'tib ketgan.")

    else:
        if request.method == "POST":
            true_answers=[]
            false_answers=[]
            al_answers={}
            for count,question in enumerate(qvv,start=1):
                answ_id=request.POST.get(str(question.id),None)
                if answ_id:
                    post_answer=Answer.objects.get(id=int(answ_id))
                    if post_answer.is_true==True:
                        al_answers[question]=[post_answer.answer,True]
                        true_answers.append(count)
                    else:
                        al_answers[question]=[post_answer.answer,False]
                        false_answers.append(count)
            
            all_qv=questions.count()
            percentage=math.floor(len(true_answers)*100/all_qv)
            text=f"{all_qv} ta savoldan {len(true_answers)} ta savolni to'g'ri topdingiz,\
                                {percentage} %"
            text2=f"Natijangiz: {percentage} %"
            if percentage>=test.pass_percentage:
                is_passed=True
            else:
                is_passed=False
            if request.user.is_authenticated:
                checktest=CheckTest.objects.create(test=test,user=request.user,
                                        true_answers=len(true_answers),
                                        percentage=percentage,is_passed=is_passed)

                messages.success(request, text)
                return redirect("check_test",checktest.id)
            else:
                messages.success(request, text2)
                # return HttpResponse(text)
                return redirect("index")
    

            


        else:
           
            return render(request, "test.html", {"qv_dict":qv_dict,"test":test})

@login_required(login_url='login')
def check_test(request, checktest_id):
    checktest = CheckTest.objects.get(id=checktest_id)
    if request.user == checktest.user:
        return render(request, "checktest.html", {"checktest":checktest})
    else:
        raise Http404("Siz ushbu testni yechmagansiz")
    
@login_required(login_url='login')
def my_results(request):
    check_tests = CheckTest.objects.filter(user=request.user).order_by("-date")
    tests = []
    for checktest in check_tests:
        if not checktest.test in tests:
            tests.append(checktest.test)
            
    return render(request, "my_results.html", {'tests':tests, "checktests":check_tests})

@login_required(login_url='login')
def results(request, test_id):
    test = Test.objects.get(id=test_id)
    if request.user == test.author:
        if request.method == "GET":
            pass
            # checktests = CheckTest.objects.filter(user=query).order_by("is_passed")

        checktests = CheckTest.objects.filter(test=test).order_by("-percentage")
        return render(request, "results.html", {"checktests":checktests, "test":test})
    else:
        messages.error(request, "Siz bu testni yaratmagansiz.")
        return redirect("index")
        


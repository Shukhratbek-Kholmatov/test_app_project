from os import name
from django.forms import ModelForm, Textarea
from .models import Test, Question,Answer
from django.utils.translation import gettext_lazy as _
class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ["title", "maximum_attemps","pass_percentage",
                  "question_count","start_date", "end_date","duration","is_anonym","is_random"]


class QuestionForm(ModelForm):
    class Meta:

        model = Question
        fields = ["question"]
        widgets = {
            'question': Textarea(attrs={'rows': 3}),
        }
        


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ["answer","is_true"]
        widgets = {
            'answer': Textarea(attrs={'rows': 2}),
        }
    

class AnswerForm2(ModelForm):
    class Meta:
        model = Answer
        fields = ["answer","is_true"]
        widgets = {
            'answer': Textarea(attrs={'rows': 2}),
        }
    
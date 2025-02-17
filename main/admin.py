from django.contrib import admin
from .models import  *
# Register your models here.

class InlineQuestion(admin.TabularInline):
    model = Question

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    model = Test
    list_display = ["id","title", "author",  "maximum_attemps","pass_percentage",
                    "question_count","is_random" ,"start_date", "end_date",
                    "duration","is_anonym"]
    inlines = [InlineQuestion]
    search_fields  = ["title"]
    list_filter = ["start_date"]
    list_per_page = 10


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ["id","test","question"]
    list_per_page = 10

    


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    model = Answer
    list_display = ["id","question","answer","is_true"]
    list_per_page = 10


@admin.register(CheckTest)
class Model(admin.ModelAdmin):
    model = CheckTest
    list_display = ["id","test","user","date","true_answers","percentage","is_passed"]
    list_filter = ["date","percentage","is_passed"]
    list_per_page = 10






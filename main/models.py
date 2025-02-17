from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
# from datetime import datetime
# Create your models here.


    
class Test(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4().hex)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="avtor")
    title = models.CharField(max_length=250, verbose_name="test nomi")
    maximum_attemps = models.PositiveIntegerField(verbose_name="maksimum urinishlar soni")
    pass_percentage = models.PositiveIntegerField(default=60,verbose_name="testdan o'tish foizi")
    question_count = models.PositiveIntegerField(verbose_name="testda tushadigan savollar soni")
    is_random = models.BooleanField(default=False,verbose_name="savollarni random chiqarish")
    start_date = models.DateTimeField(default=timezone.now, verbose_name="test boshlanish sanasi")
    end_date = models.DateTimeField(default=(timezone.now()+timezone.timedelta(days=1)), verbose_name="test tugash sanasi")
    duration = models.PositiveIntegerField(default=20, verbose_name="test yechish vaqti (minut hisobida)")
    is_anonym = models.BooleanField(default=False,verbose_name="testni bosh menyuda ko'rsatmaslik")


    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Testlar"
    

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=500, verbose_name="savol")
    def __str__(self):
        return str(f"{self.test.title}: {self.question[:50]}")
    
    class Meta:
        verbose_name = "Savol"
        verbose_name_plural = "Savollar"




class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers',verbose_name="savol")
    answer = models.CharField(max_length=500, verbose_name="variant")
    is_true=models.BooleanField(default=False, verbose_name="to'g'ri javob")
    
    def __str__(self):
        return str(f"{self.answer[:20]}")
    
    class Meta:
        verbose_name = "Variant"
        verbose_name_plural = "Variantlar"













class CheckTest(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="checktests")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True,verbose_name="test ishlangan sana")
    true_answers = models.PositiveIntegerField(default=0,verbose_name="to'g'ri javoblar soni")
    percentage = models.PositiveBigIntegerField(default=0,verbose_name="foizi")
    is_passed = models.BooleanField(default=False,verbose_name="testdan o'tdi")

    class Meta:
        verbose_name = "Natija"
        verbose_name_plural = "Natijalar"

    def __str__(self):
        return f"{str(self.test.title)}"


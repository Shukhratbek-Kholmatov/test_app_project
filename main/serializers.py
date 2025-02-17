
from rest_framework import serializers

from .models import *

from django.contrib.auth.models import User


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'
        read_only_fields = ['id', 'author']



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"

class ChecktestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckTest
        fields = "__all__"



class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

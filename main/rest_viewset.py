from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions, generics, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import *
from .models import *
from .serializers import *
from rest_framework.decorators import action

User = get_user_model()




class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.filter(is_anonym=False).order_by('id')
    serializer_class = TestSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]

    @swagger_auto_schema(
        operation_summary="Barcha testlar",
        responses={200: TestSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="My tests",
        responses={200: TestSerializer()},
    )
    @action(detail=False, methods=['get'])
    def my_tests(self, request):
        my_tests = Test.objects.filter(author=request.user).order_by('id')
        serializer = TestSerializer(my_tests, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Test questions",
        responses={200: TestSerializer()},
    )
    @action(detail=True, methods=['get'])
    def questions(self, request,pk):
        qv_answers = Test.objects.get(id=pk).questions
        serializer = QuestionSerializer(qv_answers, many=True)
        return Response(serializer.data)
    @swagger_auto_schema(
        operation_summary="Retrieve a specific Test object by ID",
        responses={200: TestSerializer()},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new Test object",
        request_body=TestSerializer,
        responses={201: TestSerializer()},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        if serializer.is_valid:
            serializer.save(author=self.request.user)

    @swagger_auto_schema(
        operation_summary="Update an existing Test object",
        request_body=TestSerializer,
        responses={200: TestSerializer()},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partially update an existing Test object",
        request_body=TestSerializer,
        responses={200: TestSerializer()},
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a specific Test object by ID",
        responses={204: "No Content"},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly2]

    @swagger_auto_schema(
        operation_summary="Question anwers",
        responses={200: TestSerializer()},
    )
    @action(detail=True, methods=['get'])
    def answers(self, request, pk):
        qv_answers = Answer.objects.filter(question=pk)
        serializer = AnswerSerializer(qv_answers, many=True)
        return Response(serializer.data)

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('id')
    serializer_class = AnswerSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly3]

class CheckTestViewSet(viewsets.ModelViewSet):
    queryset = CheckTest.objects.all().order_by('id')
    serializer_class = ChecktestSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly4]

    @swagger_auto_schema(
        operation_summary="My tests",
        responses={200: TestSerializer()},
    )
    @action(detail=False, methods=['get'])
    def my_check_tests(self, request):
        my_tests =CheckTest.objects.filter(test__author=request.user)

        serializer = ChecktestSerializer(my_tests, many=True)
        return Response(serializer.data)








class UserRegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        request_body=UserRegisterSerializer,
    )
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Foydalanuvchi muvaffaqiyatli ro‘yxatdan o‘tdi!"}, status=status.HTTP_201_CREATED)
        else:
            if 'username' in serializer.errors:
                return Response({"error": "Bu foydalanuvchi nomi allaqachon mavjud."},
                                status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





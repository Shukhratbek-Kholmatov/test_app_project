from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .rest_viewset import *
from .views import *


from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="TestMaster API",
        default_version='v1',
        description="API for managing TestMaster",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)
router = DefaultRouter()
router.register(r'tests', TestViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'checktests', CheckTestViewSet)


urlpatterns = [
    path("", index, name="index"),
    path("my-tests/", my_tests, name="my_tests" ),
    path("my-results/", my_results, name="my_results" ),
    path("create-test/", create_test, name="create_test"),
    path("create-question/<int:test_id>/", create_question, name="create_question"),
    path("create-answer/<int:question_id>/", create_answer, name="create_answer"),
    path("update-test/<int:test_id>/", update_test, name="update_test"),
    path("delete-question/<int:test_id>/<int:question_id>/", delete_question, name="delete_question"),
    path("delete-answer/<int:question_id>/<int:answer_id>/", delete_answer, name="delete_answer"),
    path("detail-test/<int:test_id>/", detail_test, name="detail_test"),
    path("update-question/<int:question_id>/", update_question, name="update_question"),
    path("ready-to-test/<int:test_id>", ready_to_test, name="ready_to_test"),#=> endpoint
    path("test/start/<int:test_id>", test, name="test"),
    path("results/<int:test_id>", results, name="results"),
    path("checktest/<int:checktest_id>", check_test, name="check_test"),


    path('api/v1/', include(router.urls)),
    path('api/v1/auth', include('djoser.urls')),
    path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/v1/register/user/', UserRegisterView.as_view(), name='register'),
]



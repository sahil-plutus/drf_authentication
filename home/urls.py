from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('stu', views.StudentAPI, basename="student_api")

urlpatterns = [
    path('', include(router.urls)),

    # when we use token authentication
    path('gettoken/', obtain_auth_token),

    # when we use session authentication
    path('auth/', include('rest_framework.urls', namespace="rest_framework"))
]

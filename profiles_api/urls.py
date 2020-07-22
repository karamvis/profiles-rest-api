from django.urls import path
from profiles_api import views


urlpatterns = [
path('helloworld/',views.HelloAPIView.as_view()),
]

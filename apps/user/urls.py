from django.urls import path
from .views import GoogleLoginView, TestApiView
from dj_rest_auth.views import LoginView, LogoutView

app_name = 'user'
urlpatterns = [
    path('google/', GoogleLoginView.as_view(), name='google'),
    path('test/', TestApiView.as_view(), name='test'),
    path('login/', LoginView.as_view()),
]

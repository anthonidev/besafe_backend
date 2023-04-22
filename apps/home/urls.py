from django.urls import path
from .views import AccountViewSet

app_name = 'home'
urlpatterns = [
    path('', AccountViewSet.as_view({'get': 'list'}), name='list'),


]

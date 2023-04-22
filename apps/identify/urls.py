from django.urls import path
from .views import AccountViewSet

app_name = 'identify'
urlpatterns = [
    path('', AccountViewSet.as_view({'get': 'list'}), name='list'),

    path('create/',
         AccountViewSet.as_view({'post': 'create'}), name='create'),
    path('update/',
         AccountViewSet.as_view({'put': 'update'}), name='update'),
]

from django.urls import path
from .views import HomeView, FloorView, GuestView

app_name = 'home'
urlpatterns = [
    # homegroup
    path('', HomeView.as_view({'get': 'list'}), name='list'),
    path(
        'create/',
        HomeView.as_view({'post': 'create'}),
        name='create'
    ),
    path(
        'update/',
        HomeView.as_view({'put': 'update'}),
        name='update'
    ),

    path(
        'guest/',
        GuestView.as_view(),
        name='guest'
    ),

    # floor
    path(
        'floor/create/<str:id>',
        FloorView.as_view(),
        name='create_floor'
    ),

    path(
        'floor/update/<str:id>',
        FloorView.as_view(),
        name='update_floor'
    ),
    path(
        'floor/delete/<str:id>',
        FloorView.as_view(),
        name='delete_floor'
    )
]

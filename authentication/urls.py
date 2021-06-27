from .views import AuthViewSet, get_user_statistics
from django.urls import path

urlpatterns = [
    path('login/', AuthViewSet.as_view({'post': 'login'})),
    path('register/', AuthViewSet.as_view({'post': 'register'})),
    path('get_user_statistics/', get_user_statistics, name='get_user_statistics'),
]

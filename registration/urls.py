from django.urls import include, path
from rest_framework import routers

from . import viewsets, views

router = routers.DefaultRouter()
router.register(r'user', viewsets.UserViewSet)
router.register(r'profile', viewsets.ProfileViewSet)

app_name = 'registration'

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
]

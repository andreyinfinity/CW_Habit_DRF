from django.urls import path
from users import views
from users.apps import UsersConfig
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


app_name = UsersConfig.name

urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
    path('', views.UserProfile.as_view(), name='profile'),

    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]

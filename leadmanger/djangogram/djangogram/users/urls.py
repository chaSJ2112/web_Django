from django.urls import path
from . import views

app_name = "users"

# views에서 main함수 호출
urlpatterns = [
    path('', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
]

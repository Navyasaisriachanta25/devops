from django.urls import path
from . import views
urlpatterns = [
   path('dash',views.dashboardpost.as_view()),
    path('user/<str:userid>/', views.get_user, name='get-user'),
    # path('create/', views.create_user, name='create-user'),
    path('login/', views.login.as_view()),   
]
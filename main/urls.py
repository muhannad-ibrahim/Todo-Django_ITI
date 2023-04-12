from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('details/<int:todo_id>', views.details),
    path('create', views.createTodo , name='create'),
    path('update/<int:todo_id>', views.updateTodo, name='update'),
    path('delete/<int:todo_id>', views.deleteTodo, name='delete'),
    path('signup', views.createUser, name='signup'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout')
]
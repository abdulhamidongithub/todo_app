from django.contrib import admin
from django.urls import path
from todos.views import all_todos, del_todo, loginView, registration, logoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', all_todos, name='all-todos'),
    path('del/<int:son>', del_todo, name='del-todo'),
    path('', loginView, name='login'),
    path('reg/', registration, name='reg'),
    path('logout/', logoutView, name='logout')
]

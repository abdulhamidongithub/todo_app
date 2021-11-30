from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Todo

def all_todos(request):
    if request.user.is_authenticated:
        todo_list = Todo.objects.filter(user=request.user)
        if request.method == 'POST':
            Todo.objects.create(
                title = request.POST['t'],
                description = request.POST['d'],
                status = request.POST['s'],
                user = request.user
            )
            return redirect('all-todos')
        return render(request, 'todo.html', {'todo_list':todo_list})
    else:
        return redirect('login')

def del_todo(request, son):
    if request.user.is_authenticated:
        if request.method == 'POST':
            item = Todo.objects.get(id=son)
            item.delete()
            return redirect('all-todos')
    else:
        return redirect('login')

def loginView(request):
    if request.method=='POST':
        l = request.POST['login']
        parol = request.POST['parol']
        user = authenticate(request, username=l, password=parol)
        if user is None:
            return redirect('login')
        else:
            login(request, user)
            return redirect('all-todos')
    return render(request, 'login.html')

def registration(request):
    if request.method=='POST':
        User.objects.create(
            username = request.POST['login'],
            password = request.POST.get('parol')
        )
        return redirect('all-todos')
    return render(request, 'reg.html')

def logoutView(request):
    logout(request)
    return redirect('login')

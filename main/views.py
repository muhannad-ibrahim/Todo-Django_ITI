from django.shortcuts import redirect, render
from .models import Todo
from .forms import TodoForm, userCreation
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def index(request):
    user = request.user
    todos = Todo.objects.filter(user=user)
    context = {
        'todos': todos,
        'user': user,
    }  

    return render(request, 'index.html', context)

def details(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    items = todo.todoitems_set.all()
    context = {
        'todo': todo,
        'items': items
    }
    return render(request, 'details.html', context)

def createTodo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'create.html', context)

def updateTodo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'create.html', context)

def deleteTodo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('/')

def createUser(request):
    form = userCreation()
    if request.method == 'POST':
        form = userCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/login')
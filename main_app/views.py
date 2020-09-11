from django.shortcuts import render, redirect
from .forms import TaskList
from .models import Task

# Create your views here.

def index(request):
    form = TaskList(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        form = TaskList()

    tasks = Task.objects.all()
    time_sum = 0
    for task in tasks:
        time_sum += task.time
    print(time_sum)
    context={
    'form':form,
    'tasks':tasks,
    'time_sum':time_sum

    }

    return render(request,'main_app/index.html', context)

def delete(request, task_id):
    task = Task.objects.get(id=task_id)

    task.delete()

    context={
    'task':task
    }

    return render(request, 'main_app/delete.html', context)

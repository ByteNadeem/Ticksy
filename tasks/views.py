from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Create your views here.


def home(request):
    """
    A view to display the home page with just the hero section
    """
    return render(request, 'tasks.html')


def tasks(request):
    """
    A view to display the tasks to do and the completed tasks
    with the tasks due soonest at the top
    """

    to_do_tasks = Task.objects.filter(completed=False).order_by('due_date')
    done_tasks = Task.objects.filter(completed=True).order_by('-due_date')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm()

    context = {
        'to_do_tasks': to_do_tasks,
        'done_tasks': done_tasks,
        'form': form,
    }

    return render(request, 'tasks_page.html', context)


def task_detail(request, task_id):
    """
    View to display a single task's details
    """
    task = get_object_or_404(Task, id=task_id)
    context = {'task': task}
    return render(request, 'task_detail.html', context)


def task_edit(request, task_id):
    """
    View to edit an existing task
    """
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)
    
    context = {'form': form, 'task': task}
    return render(request, 'task_edit.html', context)


def task_delete(request, task_id):
    """
    View to delete a task
    """
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    
    context = {'task': task}
    return render(request, 'task_confirm_delete.html', context)


def task_toggle_complete(request, task_id):
    """
    View to toggle task completion status
    """
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('tasks')

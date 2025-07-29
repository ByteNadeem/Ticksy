from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from .forms import TaskForm

# Create your views here.

def home(request):
    """
    A view to display the home page with just the hero section
    """
    return render(request, 'tasks.html')

@login_required
def tasks(request):
    """
    A view to display the tasks to do and the completed tasks
    with the tasks due soonest at the top
    """
    # Only show tasks for the current user
    to_do_tasks = Task.objects.filter(completed=False, user=request.user).order_by('due_date')
    done_tasks = Task.objects.filter(completed=True, user=request.user).order_by('-due_date')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign task to current user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('tasks')
    else:
        form = TaskForm()

    context = {
        'to_do_tasks': to_do_tasks,
        'done_tasks': done_tasks,
        'form': form,
        'is_admin': request.user.groups.filter(name='Admin').exists(),  # Check if user is admin
    }

    return render(request, 'tasks_page.html', context)

@login_required
def task_detail(request, task_id):
    """
    View to display a single task's details
    """
    task = get_object_or_404(Task, id=task_id, user=request.user)
    context = {'task': task}
    return render(request, 'task_detail.html', context)


@login_required
def task_edit(request, task_id):
    """
    View to edit an existing task
    """
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)
    
    context = {'form': form, 'task': task}
    return render(request, 'task_edit.html', context)


@login_required
def task_delete(request, task_id):
    """
    View to delete a task
    """
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('tasks')
    
    context = {'task': task}
    return render(request, 'task_confirm_delete.html', context)


@login_required
def task_toggle_complete(request, task_id):
    """
    View to toggle task completion status
    """
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    status = "completed" if task.completed else "pending"
    messages.success(request, f'Task marked as {status}!')
    return redirect('tasks')
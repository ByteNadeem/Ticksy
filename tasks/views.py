from django.shortcuts import render
from django.http import HttpResponse
from .models import Task, Category

# Create your views here.


def home(request):
    tasks = Task.objects.all().order_by('-due_date')
    categories = Category.objects.all()

    context = {
        'tasks': tasks,
        'categories': categories,
    }
    return render(request, 'tasks.html', context)

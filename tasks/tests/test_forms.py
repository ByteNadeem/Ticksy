from django.test import TestCase
from django.contrib.auth.models import User
from ..forms import TaskForm
from ..models import Category

class TaskFormTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Work')
        self.user = User.objects.create_user(username='tester', password='testpass')

    def test_task_form_valid_data(self):
        form_data = {
            'title': 'Test Task',
            'due_date': '2025-08-05',
            'category': self.category.id,
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_missing_title(self):
        form_data = {
            'title': '',
            'due_date': '2025-08-05',
            'category': self.category.id,
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_task_form_invalid_category(self):
        form_data = {
            'title': 'Test Task',
            'due_date': '2025-08-05',
            'category': 999,  # Invalid category ID
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors)
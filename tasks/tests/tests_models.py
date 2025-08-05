from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task, Category

class CategoryModelTest(TestCase):
    def test_category_str(self):
        category = Category.objects.create(name='Personal')
        self.assertEqual(str(category), 'Personal')

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='testpass')
        self.category = Category.objects.create(name='Work')

    def test_task_str(self):
        task = Task.objects.create(
            title='My Task',
            due_date='2025-08-05',
            category=self.category,
            user=self.user
        )
        self.assertEqual(str(task), 'My Task')

    def test_task_completed_default(self):
        task = Task.objects.create(
            title='Another Task',
            due_date='2025-08-06',
            category=self.category,
            user=self.user
        )
        self.assertFalse(task.completed)
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from tasks.models import Task, Category

class TaskViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='testpass')
        self.category = Category.objects.create(name='Work')
        self.task = Task.objects.create(
            title='Test Task',
            due_date='2025-08-05',
            category=self.category,
            user=self.user
        )

    def test_login_required_for_tasks_view(self):
        response = self.client.get(reverse('tasks'))
        self.assertNotEqual(response.status_code, 200)

    def test_toggle_task_completion(self):
        self.client.login(username='tester', password='testpass')
        response = self.client.post(reverse('task_toggle_complete', args=[self.task.id]))
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)
        self.assertEqual(response.status_code, 302)  # Redirect after toggle

    def test_user_cannot_toggle_other_users_task(self):
        other_user = User.objects.create_user(username='other', password='otherpass')
        self.client.login(username='other', password='otherpass')
        response = self.client.post(reverse('task_toggle_complete', args=[self.task.id]))
        self.assertEqual(response.status_code, 404)

    def test_create_task(self):
        self.client.login(username='tester', password='testpass')
        response = self.client.post(reverse('tasks'), {
            'title': 'New Task',
            'due_date': '2025-08-10',
            'category': self.category.id,
        })
        self.assertEqual(Task.objects.filter(title='New Task').count(), 1)

    def test_delete_task(self):
        self.client.login(username='tester', password='testpass')
        response = self.client.post(reverse('task_delete', args=[self.task.id]))
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())
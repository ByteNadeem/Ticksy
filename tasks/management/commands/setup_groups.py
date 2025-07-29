from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from tasks.models import Task

class Command(BaseCommand):
    help = 'Create user groups with permissions'

    def handle(self, *args, **options):
        # Create Admin group
        admin_group, created = Group.objects.get_or_create(name='Admin')
        if created:
            self.stdout.write(self.style.SUCCESS('Created Admin group'))
        
        # Create Regular User group
        user_group, created = Group.objects.get_or_create(name='Regular User')
        if created:
            self.stdout.write(self.style.SUCCESS('Created Regular User group'))
        
        # Get Task permissions
        task_content_type = ContentType.objects.get_for_model(Task)
        
        # Admin gets all permissions
        admin_permissions = Permission.objects.filter(content_type=task_content_type)
        admin_group.permissions.set(admin_permissions)
        
        # Regular users get basic permissions
        user_permissions = Permission.objects.filter(
            content_type=task_content_type,
            codename__in=['add_task', 'change_task', 'delete_task', 'view_task']
        )
        user_group.permissions.set(user_permissions)
        
        self.stdout.write(self.style.SUCCESS('Successfully set up user groups and permissions'))
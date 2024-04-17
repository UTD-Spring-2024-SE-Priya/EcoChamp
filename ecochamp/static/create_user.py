from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a user'

    def handle(self, *args, **options):
        # Create the user
        user = User.objects.create_user(username='oldUserPerson', email='olduser3354@gmail.com', password='oldchamp')
        # Save the user
        user.save()
        self.stdout.write(self.style.SUCCESS('User created successfully'))

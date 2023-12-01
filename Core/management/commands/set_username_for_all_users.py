from django.core.management.base import BaseCommand
from django.db import transaction

from Core.models import User


class Command(BaseCommand):
    help = 'Set \'No Human\' in username model field for each User'

    @transaction.atomic
    def handle(self, *args, **options):
        users = User.objects.all()
        users.update(username='No Human')
        print(f'{len(users)} users was updated.')


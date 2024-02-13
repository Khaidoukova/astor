from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='olga@noran.ru',
            office_number=601,
            company='NORAN',
            name='Ольга Хайдукова',
            phone='+79222244847',
            is_staff=True,
            is_superuser=True,
            is_manager=True,


        )

        user.set_password('320670')
        user.save()
        print('superuser created')

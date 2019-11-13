from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):

    help = "This command create many users"

    def add_arguments(seld, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many users do you want to create"
        )

    def handle(self, *args, **options):

        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {
            "is_staff": False,
            "is_superuser": False
        })
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))


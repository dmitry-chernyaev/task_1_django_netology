import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            Phone(
                id=int(phone['id']),
                name=phone['name'],
                price=int(phone['price']),
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists']
            ).save()
        self.stdout.write(self.style.SUCCESS(f'Imported {len(phones)} phones'))
        # Когда вы вызываете phone.save():
        # 1. Django вызывает ваш кастомный метод save() из модели
        # 2. В нем выполняется: self.slug = slugify(self.name)
        # 3. Затем вызывается стандартный save() родительского класса
        # 4. Объект сохраняется в базу с автоматически созданным slug


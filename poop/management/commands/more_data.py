from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):

    def handle(self, *args, **options,):
            
        self.stdout.write('Add data to prompts table...')
        call_command('prompts_seeder')
        self.stdout.write(self.style.SUCCESS('✅ Data successfully added.'))

        self.stdout.write('Add data to cards table...')
        call_command('cards_seeder')
        self.stdout.write(self.style.SUCCESS('✅ Data successfully added.'))

        self.stdout.write('Add data to collections table...')
        call_command('collections_seeder')
        self.stdout.write(self.style.SUCCESS('✅ Data successfully added.'))

        self.stdout.write('Add data to scores table...')
        call_command('scores_seeder')
        self.stdout.write(self.style.SUCCESS('✅ Data successfully added.'))

        self.stdout.write(self.style.SUCCESS('\n\n ✅ Database has been filled successfully!\n'))
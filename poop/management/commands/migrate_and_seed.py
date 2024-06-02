from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Flushing the database...')
        call_command('flush', '--no-input')
        self.stdout.write(self.style.SUCCESS('✅ Database has been flushed.'))
        
        self.stdout.write('Applying migrations...')
        call_command('migrate')
        self.stdout.write(self.style.SUCCESS('✅ Migrations applied successfully.'))
        
        self.stdout.write('Seeding the users table...')
        call_command('users_seeder')
        self.stdout.write(self.style.SUCCESS('✅ Users table seeded successfully.'))

        self.stdout.write('Seeding the draws table...')
        call_command('draws_seeder')
        self.stdout.write(self.style.SUCCESS('✅ Draws table seeded successfully.'))

        self.stdout.write('Seeding the prompts table...')
        call_command('prompts_seeder')
        self.stdout.write(self.style.SUCCESS('✅ Prompts table seeded successfully.'))

        self.stdout.write('Seeding the cards table...')
        call_command('cards_seeder')
        self.stdout.write(self.style.SUCCESS('✅ Cards table seeded successfully.'))

        self.stdout.write('Seeding the collections table...')
        call_command('collections_seeder')
        self.stdout.write(self.style.SUCCESS('✅ Collections table seeded successfully.'))

        self.stdout.write('Seeding the scores table...')
        call_command('scores_seeder')
        self.stdout.write(self.style.SUCCESS('✅ Scores table seeded successfully.'))

        self.stdout.write(self.style.SUCCESS('\n\n ✅ Database has been flushed, migrated, and seeded successfully!\n'))
from django.core.management.base import BaseCommand
from poop.models import Card, User, Prompt


class Command(BaseCommand):

    def handle(self, *args, **options):

        prompts_list = Prompt.objects.get_all_prompts()
        users_list = User.objects.get_all_users()

        for prompt in prompts_list:
            for user in users_list:
                Card.objects.create_card(prompt_id=prompt.id, generated_by=user, image_path="")

        

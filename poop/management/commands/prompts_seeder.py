from django.core.management.base import BaseCommand
from poop.models import Prompt, User
from poop.scripts.prompt_generator import generate_prompt


class Command(BaseCommand):

    def handle(self, *args, **options):
        prompts_list = []
        while len(prompts_list) < 4:
            prompt = generate_prompt()
            prompts_list.append(prompt)

        
        for prompt in prompts_list:
            Prompt.objects.create(text=prompt)

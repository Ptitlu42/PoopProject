from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from poop.scripts.image_generator import generate_image
import re


class UserManager(BaseUserManager):
    def create_user(self, phone_number, name, password, mail):
        user = self.model(phone_number=phone_number, name=name, password=password, mail=mail)
        user.save(using=self._db)
        print('Created user:', user.name)

    def delete_user (self):
        user = self.model()
        user.delete()
        print ('Deleted user:', user.name)

    def update_user (self, phone_number, name, password, mail):
        user = self.model()
        user.save()

    def get_user_by_phone_number(self, phone_number):
        user = self.get_queryset().get(phone_number=phone_number)
        return user

    def get_user_by_id(self, user_id):
        user = self.get_queryset().get(id=user_id)
        return user

    def get_all_users(self):
        users = self.get_queryset()
        return users

class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    mail = models.EmailField(unique=True)
    user_since = models.DateTimeField(auto_now_add=True)
    total_draw = models.IntegerField(default=0)

    objects = UserManager()

    def __str__(self):
        return self.name

class DrawManager(models.Manager):
    def create_draw(self, user):
        draw = self.model(user=user)
        draw.save()
        print ('Created draw for user', user)

    def add_draw_count(self, user, draw_count):
        draw = self.model(user=user, draw_count=draw_count)
        draw.draw_count += 1
        draw.save()
        print('Added draw count for user', user.name, 'count:', draw.draw_count)

    def get_draw(self, user):
        draw = self.model(user=user)
        return draw

class Draw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='draws')
    date = models.DateTimeField(auto_now_add=True, verbose_name="Draw date")
    draw_count = models.IntegerField(default=0, verbose_name="Draw count")

    objects = DrawManager()
    def __str__(self):
        return f"Draw {self.id} - User {self.user.name} - Count {self.draw_count}"

class ScoreManager(models.Manager):
    def create_score(self, user):
        score, created = self.get_or_create(user=user)

        unique_cards_count = user.collections.values('card').distinct().count()

        score.unique_card_count = unique_cards_count
        score.save()

        if created:
            print('Created score for user:', user.name)
            self.update_ranks()
        else:
            print('Updated unique card count for user:', user.name, 'count:', unique_cards_count)
            self.update_ranks()


    def get_score_by_id(self, user_id):
        score = self.get_queryset().get(user_id=user_id)
        return score

    def update_ranks(self):
        pass

class Score (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scores')
    unique_card_count = models.IntegerField(default=0, verbose_name="Unique card count")
    rank = models.IntegerField(default=0, verbose_name="Rank")

    objects = ScoreManager()
    def __str__(self):
        return f"Score {self.id} - User {self.user.name} - Rank {self.rank}"

class PromptManager(models.Manager):
    def create_prompt(self, text):
        if not self.get_queryset().filter(text=text).exists():
            prompt = self.model(text=text)
            prompt.save()
            print('Prompt created: ', text)

        else:
            print('Prompt already exists: ', text)

    def delete_prompt_by_id(self, prompt_id):
        prompt = self.get_queryset().get(id=prompt_id)
        prompt.delete()
        print('Prompt deleted: ', prompt.text)

    def get_prompt_by_id(self, prompt_id):
        prompt = self.get_queryset().get(id=prompt_id)
        return prompt

    def get_text_by_id(self, prompt_id):
        prompt = self.get_queryset().get(id=prompt_id)
        return prompt.text

    def get_all_prompts(self):
        prompts = self.get_queryset()
        return prompts


class Prompt(models.Model):
    text = models.TextField()
    generated_date = models.DateTimeField(auto_now_add=True)

    objects = PromptManager()

    def __str__(self):
        return self.text

class CardManager(models.Manager):

    def create_card(self, prompt_id, generated_by):
        prompt = Prompt.objects.get(id=prompt_id)
        prompt_text = prompt.text
        draw_count = Draw.objects.get_draw(generated_by).draw_count
        if draw_count < 4:
            if not self.get_queryset().filter(prompt=prompt).exists():
                image_path = generate_image(prompt_text)
                
                card = self.model(
                    prompt=prompt,
                    generated_by=generated_by,
                    image_path=image_path
                )

                user = generated_by
                card.save()
                Collection.objects.add_card_to_user_collection(generated_by, card)
                Draw.objects.add_draw_count(generated_by, 1)
                return None

        else :
            print('Draw count exceeded for ', user.name)

    

    def delete_card_by_id(self, card_id):
        card = self.get_queryset().get(id=card_id)
        card.delete()
        print('Card deleted: ', card.prompt.text)

    def get_card_by_id(self, card_id):
        card = self.get_queryset().get(id=card_id)
        return card

    def get_card_by_prompt_id(self, prompt_id):
        card = self.get_queryset().get(prompt_id=prompt_id)
        return card

    def get_all_cards(self):
        cards = self.get_queryset()
        return cards

    def get_all_cards_by_user_id(self, user_id):
        cards = self.get_queryset().filter(generated_by=user_id)
        return cards

    def get_cards_by_user_id(self, user_id):
        cards = self.get_queryset().filter(generated_by=user_id)
        return cards

class Card (models.Model):
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE, related_name='cards')
    generated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cards')
    image_path = models.FilePathField()
    total_draw = models.IntegerField(default=0)

    objects = CardManager()

    def __str__(self):
        return f"Card {self.id} - Prompt {self.prompt_id} - User {self.generated_by.name}"

class CollectionManager(models.Manager):
    def create_collection(self):
        collection = self.model()
        collection.save()
        print('Created collection for user:', collection.user.name, 'at', collection.owned_since)

    def delete_collection_by_id(self, collection_id):
        collection = self.get_queryset().get(id=collection_id)
        collection.delete()
        print('Collection deleted for user:', collection.user.name, 'at', collection.owned_since)

    def get_collection_by_id(self, collection_id):
        collection = self.get_queryset().get(id=collection_id)
        return collection

    def get_collection_by_user_id(self, user_id):
        collections = self.get_queryset().filter(user_id=user_id)
        return collections

    def add_card_to_user_collection(self, user, card):
        collection, created = Collection.objects.get_or_create(user=user, card=card)
        collection.quantity += 1
        collection.save()
        print('Card: "', card.prompt.text, '" added to collection for user:', collection.user.name)
    
class Collection (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collections')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='collections')
    quantity = models.IntegerField(default=0)
    owned_since = models.DateTimeField(auto_now_add=True)

    objects = CollectionManager()

    def __str__(self):
        return f"Collection {self.id} - User {self.user.name} - Card {self.card.prompt_id}"

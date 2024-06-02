from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number):
        user = self.model(phone_number=phone_number)
        user.save(using=self._db)

    def delete_user (self, phone_number):
        user = self.model(phone_number=phone_number)
        user.delete()

    def update_user (self, phone_number, name, password, mail):
        user = self.model(phone_number=phone_number)
        user.save()

    def get_user_by_phone_number(self, phone_number):
        user = self.get_queryset().get(phone_number=phone_number)
        return user

    def get_user_by_id(self, user_id):
        user = self.get_queryset().get(id=user_id)
        return user

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

    def add_draw_count(self, user, draw_count):
        draw = self.model(user=user, draw_count=draw_count)
        draw.draw_count += 1
        draw.save()

    def get_draw(self, user):
        draw = self.model(user=user)
        return draw

class Draw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='draws')
    date = models.DateTimeField(auto_now_add=True, verbose_name="Draw date")
    draw_count = models.IntegerField(default=0, verbose_name="Draw count")

    def __str__(self):
        return f"Draw {self.id} - User {self.user.name} - Count {self.draw_count}"

class ScoreManager(models.Manager):
    def create_score(self):
        score = self.model()
        score.save()

    def add_card_count (self, unique_card_count):
        score = self.model(unique_card_count=unique_card_count)
        score.unique_card_count += 1
        score.save()

    def get_score_by_id(self, user_id):
        score = self.get_queryset().get(user_id=user_id)
        return score


class Score (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scores')
    unique_card_count = models.IntegerField(default=0, verbose_name="Unique card count")
    rank = models.IntegerField(default=0, verbose_name="Rank")

    def __str__(self):
        return f"Score {self.id} - User {self.user.name} - Rank {self.rank}"

class PromptManager(models.Manager):
    def create_prompt(self, text):
        prompt = self.model(text=text)
        prompt.save()

    def delete_prompt_by_id(self, prompt_id):
        prompt = self.get_queryset().get(id=prompt_id)
        prompt.delete()

    def get_prompt_by_id(self, prompt_id):
        prompt = self.get_queryset().get(id=prompt_id)
        return prompt


class Prompt(models.Model):
    text = models.TextField()
    generated_date = models.DateTimeField(auto_now_add=True)

    objects = PromptManager()

    def __str__(self):
        return self.text

class CardManager(models.Manager):
    def create_card(self):
        card = self.model()
        card.save()

    def delete_card_by_id(self, card_id):
        card = self.get_queryset().get(id=card_id)
        card.delete()

    def get_card_by_id(self, card_id):
        card = self.get_queryset().get(id=card_id)
        return card

    def get_card_by_prompt_id(self, prompt_id):
        card = self.get_queryset().get(prompt_id=prompt_id)
        return card

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

    def delete_collection_by_id(self, collection_id):
        collection = self.get_queryset().get(id=collection_id)
        collection.delete()

    def get_collection_by_id(self, collection_id):
        collection = self.get_queryset().get(id=collection_id)
        return collection

    def get_collection_by_user_id(self, user_id):
        collections = self.get_queryset().filter(user_id=user_id)
        return collections
    

class Collection (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collections')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='collections')
    quantity = models.IntegerField(default=0)
    owned_since = models.DateTimeField(auto_now_add=True)

    objects = CollectionManager()

    def __str__(self):
        return f"Collection {self.id} - User {self.user.name} - Card {self.card.prompt_id}"
# Generated by Django 5.0.6 on 2024-06-02 11:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poop', '0002_draw'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_card_count', models.IntegerField(default=0, verbose_name='Unique card count')),
                ('rank', models.IntegerField(default=0, verbose_name='Rank')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='poop.user')),
            ],
        ),
    ]

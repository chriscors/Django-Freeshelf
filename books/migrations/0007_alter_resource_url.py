# Generated by Django 4.1.7 on 2023-03-13 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_user_favorite_stories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='url',
            field=models.CharField(blank=True, max_length=400, null=True, unique=True),
        ),
    ]

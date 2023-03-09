# Generated by Django 4.1.7 on 2023-03-08 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_category_alter_resource_options_resource_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='resource',
            name='img_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='url',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
    ]
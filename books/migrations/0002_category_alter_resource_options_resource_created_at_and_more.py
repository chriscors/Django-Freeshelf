# Generated by Django 4.1.7 on 2023-03-08 05:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(default='djangodbmodelsfieldscharfield')),
            ],
        ),
        migrations.AlterModelOptions(
            name='resource',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='resource',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='img_url',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='url',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.category'),
        ),
    ]

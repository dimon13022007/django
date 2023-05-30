# Generated by Django 4.1.7 on 2023-03-22 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва завдання')),
                ('text', models.CharField(max_length=80, verbose_name='Текст завдання')),
                ('answer', models.TextField(max_length=400, verbose_name='Відповідь до завдання')),
                ('date', models.DateTimeField(verbose_name='Дата публікації')),
                ('hard_easy', models.CharField(max_length=40, verbose_name='Рівень складності')),
            ],
        ),
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новина', 'verbose_name_plural': 'Новини'},
        ),
    ]
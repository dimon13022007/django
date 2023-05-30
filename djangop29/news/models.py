from django.db import models


class Articles(models.Model):
    title = models.CharField('Назва', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Стаття')
    date = models.DateTimeField('Дата публікації')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'


class Tasks(models.Model):
    title = models.CharField('Назва завдання', max_length=50)
    text = models.CharField('Текст завдання', max_length=80)
    answer = models.TextField('Відповідь до завдання', max_length=400)
    date = models.DateTimeField('Дата публікації')
    hard_easy = models.CharField('Рівень складності', max_length=40)

    def __str__(self):
        return self.title




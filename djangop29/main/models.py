from django.db import models
from django.contrib.auth.models import User

class About3(models.Model):
    title = models.CharField('Електронна пошта', max_length=100)
    anons = models.CharField('Телефон', max_length=15)
    full_text = models.TextField("ім'я", max_length=20)
    age = models.IntegerField('вік')
    Happy_or_not = models.FloatField('Рівень щастя від 1 до 10')
    Have_car_or_not = models.BooleanField('Машина є?')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'





class UserAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)









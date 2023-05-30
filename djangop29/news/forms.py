from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput
from .models import Tasks


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title':TextInput(attrs={
                'class':'form-control',
                'placeholder' : "Назва"

            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Анонс"
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': "Дата і час"
            }),
            'full_text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Повний час"
            }),

            }
class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'text', 'answer', 'date', 'hard_easy']

        widgets = {
            'title':TextInput(attrs={
                'class':'form-control',
                'placeholder' : "Назва"

            }),
            'text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Анонс"
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': "Дата і час"
            }),
            'answer': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Повний час"
            }),

            'hard_easy': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Повний час"
            }),

            }

       #  Даний
       #  алгоритм  описує два   класи  форми: ArticlesForm і  TasksForm.Кожен  з цих класів  є
       #  похідним  від  ModelForm і використовується для створення  форми  на  основі
       #  відповідної  моделі     Articles   і  Tasks.   У
       #  класі  ArticlesForm, властивість  Meta  визначає   метадані   форми.Вона    вказує
       #  модель, з   якої   треба    створити  форму(model=Articles), а     також   перелік   полів, які   будуть  відображені
       # у   формі    Далі, для   кожного   поля   форми    використовується   відповідний   віджет(widget), який  визначає
       #  зовнішній  вигляд   і   поведінку   поля.Наприклад, полю title встановлюється   текстове   поле  з   класом
       #  form - control  і     плейсхолдером     Аналогічно, в  класі   TasksForm  виконується  аналогічний
       #  процес  для   полів   моделі
       #  Tasks.   Цей   код   використовує   TextInput   та  DateTimeInput  для текстових   полів   і   полів   дати / часу   відповідно, а  також
       #  встановлює  клас  form - control  для стилізації полів  за  допомогою  Bootstrap.
       #  Таким   чином, цей  код   визначає  форми
       #  ArticlesForm  і  TasksForm  з  відповідними  полями   і   віджетами  для  кожного   поля.
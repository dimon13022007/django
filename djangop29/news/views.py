from django.shortcuts import render, redirect
from .models import Articles
from .models import Tasks
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView


def news_home(request):
    news = Articles.objects.order_by('-date')

    return render(request, 'news/news_home.html', {'news':news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'


class NewsUpdateView():
    model = Articles
    template_name = 'news/create.html'




def tasks(request):

    tasks = Tasks.objects.order_by()
    return render(request, 'news/tasks.html', {'tasks':tasks})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Не работает, значит фигню написал"
    form = ArticlesForm()
    data = {
        'form':form,
        'error':error,
    }
    return render(request, 'news/create.html', data)

def create_task(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Не работает, значит фигню написал"
    form = ArticlesForm()
    data = {
        'form':form,
        'error':error,
    }
    return render(request, 'news/create_task.html', data)






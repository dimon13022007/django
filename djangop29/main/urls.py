from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),

    path('cost/', views.about, name='about'),
    path('kids/', views.contact),
    path('payments/', views.payments),
    path('successful/', views.payments2),

    path('contacts/', views.contacts)



]

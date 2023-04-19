from django.urls import path

from . import views

app_name = 'celery_email'
urlpatterns = [
    path('reminder/', views.sender, name='reminder'),
    path('success/', views.success, name='success'),

]
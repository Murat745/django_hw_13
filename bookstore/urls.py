from django.urls import path

from . import views

app_name = 'bookstore'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>', views.book, name='book'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:pk>', views.author, name='author'),
    path('publishers/', views.publisher_list, name='publisher_list'),
    path('publishers/<int:pk>', views.publisher, name='publisher'),
    path('stores/', views.store_list, name='store_list'),
    path('stores/<int:pk>', views.store, name='store'),

]

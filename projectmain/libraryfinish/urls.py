from django.urls import path

from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('authors/', views.authors, name='authors'),
    path('publishers/', views.publishers, name='publishers'),
    path('books/<str:pk>', views.book, name='book'),
    path('add-book/', views.addBook, name='add-book'),
    path('edit-book/<str:pk>', views.editBook, name='edit-book'),
    path('add-author/', views.addAuthor, name='add-author'),
    path('add-publisher/', views.addPublisher, name='add-publisher')
]
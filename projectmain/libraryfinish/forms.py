from django.forms import ModelForm

from .models import Books, Author, Publisher


class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author', 'publisher', 'cover']


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email',]

    
class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'address']
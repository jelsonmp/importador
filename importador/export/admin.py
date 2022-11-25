from django.contrib import admin

# Register your models here.
from import_export import resources
from core.models import Book

class BookResource(resources.ModelResource):

    class Meta:
        model = Book
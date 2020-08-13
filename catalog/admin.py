from django.contrib import admin

from .models import Author, Genre, Book

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)



class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
admin.site.register(Author, AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author')


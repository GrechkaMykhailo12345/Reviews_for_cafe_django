from django.contrib import admin
from .models import Review
from django.contrib.auth.models import User

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'content')
    list_filter = ('pub_date', 'author')
    search_fields = ('title', 'content')
    date_hierarchy = 'pub_date'
from django.contrib import admin
from .models import BlogPost

# Register your models here.

# this regesters the model to the admin site
class BlogDataAdmin(admin.ModelAdmin):
    # conent_display = (
    #     'title',
    #     'slug',
    #     'updated_on',
    #     'content',
    #     'created_on',
    #     'status',
    #     )
    # this lets the data show in the admin site 
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(BlogPost, BlogDataAdmin)
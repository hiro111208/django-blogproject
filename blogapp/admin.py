from django.contrib import admin

# Register your models here.
from .models import BlogPost

# Register BlogPost model to admin site
admin.site.register(BlogPost)

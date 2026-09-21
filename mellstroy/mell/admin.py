from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Quotes)
admin.site.register(Category)
admin.site.register(Quote_Category)
admin.site.register(Tags)
admin.site.register(Quote_Tag)
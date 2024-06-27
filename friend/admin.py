from django.contrib import admin
from .models import Hello

# Register your models here.
class HelloAdmin(admin.ModelAdmin):
    list_display=('name','dob')
admin.site.register(Hello,HelloAdmin)


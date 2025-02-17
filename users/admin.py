from django.contrib import admin
from .models import Profile
# Register your models here.









@admin.register(Profile)
class TestAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ["id","user","bio","anonym", "picture"]
   



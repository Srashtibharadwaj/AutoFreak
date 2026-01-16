from django.contrib import admin
from .models import register
from .models import carrental
from .models import mechanic


# Register your models here.
class registerModel(admin.ModelAdmin):
    list_display=["email"]
admin.site.register(register,registerModel)
admin.site.register(carrental)
admin.site.register(mechanic)

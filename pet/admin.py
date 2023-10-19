from django.contrib import admin

from .models import Pet, Shelter


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'shelter']
    list_filter = ['name']

    def __str__(self):
        return self.name


@admin.register(Shelter)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'located_at']
    list_filter = ['name']

    def __str__(self):
        return self.name

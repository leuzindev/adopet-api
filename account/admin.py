from django.contrib import admin

from .models import User, Tutor, Organization


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_superuser')
    list_filter = ['username']

    def __str__(self):
        return self.username


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('user',)

    def __str__(self):
        return self.user


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('user',)

    def __str__(self):
        return self.user

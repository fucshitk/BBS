from django.contrib import admin

from App.models import User


class userAdmin(admin.ModelAdmin):
    list_display = [
        'uname',
        'uicon',
    ]

admin.site.register(User,userAdmin)

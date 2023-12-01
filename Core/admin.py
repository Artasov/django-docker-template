from django.contrib import admin

from Core.models import User

# ADMIN SETTINGS
admin.site.site_title = 'admin'
admin.site.site_header = 'xlartas admin'
admin.site.index_title = 'xlartas'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)

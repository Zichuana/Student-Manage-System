from django.contrib import admin

from .models import UserInfo, StuInfo


# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['UserId', 'username', 'password']


class StuInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'stuname', 'stuphone', 'stuaddress', 'stucollege', 'stumajor']


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(StuInfo, StuInfoAdmin)

# Register your models here.
# python manage.py createsuperuser


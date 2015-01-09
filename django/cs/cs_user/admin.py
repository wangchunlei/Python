from django.contrib import admin
from cs_user.models import User, Account

# Register your models here.


class AccountInline(admin.StackedInline):

    """docstring for AccountInline"""
    model = Account
    extra = 3


class UserAdmin(admin.ModelAdmin):

    """docstring for UserAdmin"""
    fieldsets = [
        (None, {'fields': ['user_code', 'user_name']}),
    ]

    list_display = ('user_code', 'user_name')
    inlines = [AccountInline]


admin.site.register(User, UserAdmin)

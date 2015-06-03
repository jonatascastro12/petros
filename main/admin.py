from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from main.models import UserProfile, ChurchAccount, Church, ChurchType


class ChurchAccountAdmin(admin.ModelAdmin):
    model = ChurchAccount

class ChurchTypeAdmin(admin.ModelAdmin):
    model = ChurchType

class ChurchAdmin(admin.ModelAdmin):
    model = Church

class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(is_superuser=False)

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return super(UserAdmin, self).get_fieldsets(request, obj)
        else:
            return (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(ChurchAccount, ChurchAccountAdmin)
admin.site.register(Church, ChurchAdmin)
admin.site.register(ChurchType, ChurchTypeAdmin)
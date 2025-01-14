from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Company, Requete,FinancialControlSubmission
from unfold.admin import ModelAdmin

from django.contrib.admin import register
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm


class CustomUserAdmin(UserAdmin,ModelAdmin):
    model = CustomUser
    list_display = ('email', 'role', 'is_staff', 'is_superuser')
    search_fields = ('email', 'role', 'first_name', 'last_name')
    ordering = ('email',)
    readonly_fields = ('id', 'last_login')
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('role', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


class FinancialAdmin(ModelAdmin):
    list_display = ['id', 'requete', 'created_at']
    search_fields = ['requete__id', 'grand_livre_status']
    list_filter = ['created_at']


class RequeteAdmin(ModelAdmin):
    list_display = ('reference', 'company', 'responsable', 'consultant', 'date','completed')  # Adjusted field names
    search_fields = ('reference', 'company__name', 'responsable__email', 'consultant__email')  # Add fields you want to be searchable

class CompanyAdmin(ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')
    ordering = ('name',)





# Registering the admin classes with their respective models
admin.site.register(Company, CompanyAdmin)

# Unregister the CustomUser model if it is already registered
if admin.site.is_registered(CustomUser):
    admin.site.unregister(CustomUser)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Requete, RequeteAdmin)
admin.site.register(FinancialControlSubmission,FinancialAdmin)
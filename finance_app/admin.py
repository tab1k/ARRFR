from django.contrib import admin
from finance_app.models import *


@admin.register(FinancialOrganization)
class FinancialOrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'bin', 'address', 'phone', 'email', 'website', 'active')
    list_filter = ('bin', 'active')
    search_fields = ('name', 'bin', 'email', 'active')


@admin.register(Executive)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('financial_organization', 'full_name', 'iin', 'position', 'contact_phone', 'contact_email', 'start_date', 'end_date')
    list_filter = ('financial_organization', 'iin', 'position')
    search_fields = ('financial_organization', 'full_name', 'iin', 'position')


admin.site.register(UserPosition)
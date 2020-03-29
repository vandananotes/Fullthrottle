from django.contrib import admin
from .models import *

class ActivityPeriodAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time')


class UserAdmin(admin.ModelAdmin):
    list_display = ('real_name', 'activity_periods_id')

admin.site.register(ActivityPeriod, ActivityPeriodAdmin)
admin.site.register(User, UserAdmin)
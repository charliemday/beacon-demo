from django.contrib import admin

from .models import PromptLog

# Register your models here.


class PromptLogAdmin(admin.ModelAdmin):
    list_display = ("prompt", "result", "tokens", "modified")


admin.site.register(PromptLog, PromptLogAdmin)

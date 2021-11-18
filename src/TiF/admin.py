from django.contrib import admin
from . import models


admin.site.register(models.User)
admin.site.register(models.Category)
admin.site.register(models.Foundation)
admin.site.register(models.Comment)
admin.site.register(models.Text)
admin.site.register(models.Mpaa)
admin.site.register(models.Message)
admin.site.register(models.Choice)
admin.site.register(models.TextDep)
admin.site.register(models.Hashtag)

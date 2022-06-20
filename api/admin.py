from django.contrib import admin
# models
from . import models



# ADMIN Panel
admin.site.register(models.user.User)
admin.site.register(models.item.Item)
admin.site.register(models.category.Category)
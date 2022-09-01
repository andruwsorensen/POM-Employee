from django.contrib import admin

from .models import Checklist, Item, Template, Items

admin.site.register(Checklist)
admin.site.register(Template)
admin.site.register(Items)
admin.site.register(Item)
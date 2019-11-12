from django.contrib import admin
from .models import Recepmodel,Query
# Register your models here.
class RecepmodelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Recepmodel, RecepmodelAdmin)

class QueryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Query, QueryAdmin)







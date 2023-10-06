from django.contrib import admin
from .models import Namespace, Node, FieldRelation, Scheme

# Register your models here.


@admin.register(Namespace)
class NamespaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    exclude = ('complete_name',)


@admin.register(FieldRelation)
class FieldRelationAdmin(admin.ModelAdmin):
    pass


@admin.register(Scheme)
class SchemeAdmin(admin.ModelAdmin):
    pass


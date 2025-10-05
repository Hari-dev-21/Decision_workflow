from django.contrib import admin
from .models import Workflow, Node, Edge

class NodeInline(admin.TabularInline):
    model = Node
    extra = 1

class EdgeInline(admin.TabularInline):
    model = Edge
    fk_name = 'from_node'
    extra = 1

@admin.register(Workflow)
class WorkflowAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [NodeInline]

@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'workflow']
    inlines = [EdgeInline]

@admin.register(Edge)
class EdgeAdmin(admin.ModelAdmin):
    list_display = ['id', 'from_node', 'to_node', 'condition']

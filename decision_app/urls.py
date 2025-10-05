from django.urls import path
from . import views

 
urlpatterns = [
    path('', views.workflow_list, name='workflow_list'),
    path('workflow_detail/<int:workflow_id>/', views.workflow_detail, name='workflow_detail'),
    path('add_node/<int:workflow_id>/', views.add_node, name='add_node'),
    path('add_edge/<int:workflow_id>/', views.add_edge, name='add_edge'),
    path('add_workflow/', views.add_workflow, name='add_workflow'),
    path('start_workflow/<int:workflow_id>/', views.start_workflow, name='start_workflow'),
    path('view_node/<int:node_id>/', views.view_node, name='view_node'),
    path('visualize_workflow/<int:workflow_id>/', views.visualize_workflow, name='visualize_workflow'),



    path('delete_workflow/<int:workflow_id>/', views.delete_workflow, name='delete_workflow'),

    
] 
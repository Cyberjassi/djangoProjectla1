from django.urls import path
from . import views
urlpatterns = [
     path('',views.projects,name = "projects"),
    path('project/<str:pk>/',views.project,name="project"),
    path('create-project/',views.createProjects,name="create-project"),
    path('update-project/<str:pk>',views.updateProjects,name="update-project"),
    path('delete-project/<str:pk>',views.deleteProjects,name="delete-project"),
    
]

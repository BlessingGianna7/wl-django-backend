from django.urls import path
from .views import guider_list, add_guider, edit_guide, delete_guider

urlpatterns = [
    path('', guider_list, name='guider_list'),  
    path('add/', add_guider, name='add_guider'),  
    path('edit/<int:guide_id>/', edit_guide, name='edit_guide'), 
    path('delete/<int:guide_id>/', delete_guider, name='delete_guider'),
]

from django.urls import path
from .views import *


urlpatterns = [
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('main/', first, name='main'),
    path('submissions/', submission_list, name='submission_list'),

    path('immofi/', submission_create, name='submission_create'),
    path('immofi/<int:pk>/edit/', submission_update, name='submission_update'),
    path('immofi/<int:pk>/delete/', submission_delete, name='submission_delete'),
    path('requete/confirm/<int:requete_id>/', confirm_requete, name='requete_confirm'),
    path('submission/<int:submission_id>/download/', download_submission_pdf, name='submission_download_pdf'),
    

    
  

   
]

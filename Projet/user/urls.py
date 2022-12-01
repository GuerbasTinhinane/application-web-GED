from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user.views import view_history, dashboard
from user.views import home, logoutUser, register, chefdep, juriste, admin
from user.views import update_user, update_accord, update_partenaire_fdup, update_accordOp, update_avenant, update_avis,  update_contrat, update_convention, update_lettreAccord, update_pds, update_st 
from user.views import  affiche_detail_accord
from user.views import  PasswordsChangeView
from user.views import delete_user, delete_accord, delete_partenaire, delete_fdup, delete_accordOp, delete_avenant, delete_avis,  delete_contrat, delete_convention, delete_lettreAccord, delete_pds, delete_st 
from user.views import accord_create, accordOperation_create, avenant_create, avisJuridique_create, contrat_create, convention_create, lettreAccord_create, pds_create, st_create
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', home, name="home"),
    path('logoutUser', logoutUser, name="logoutUser"),
    path('register', register, name='register'),
    path('chefdep', chefdep, name='chefdep'),
    path('juriste', juriste, name='juriste'),
    path('admin', admin, name='admin'),
    path('dashboard', dashboard, name="dashboard"),
    path('map', views.index, name='dashboard-index'),
    #path affiche
    # path('affiche_accord', affiche_accord, name='affiche_accord'),
    # path('affiche_accordOp', affiche_accordOp, name='affiche_accordOp'),
    # path('affiche_avenant', affiche_avenant, name='affiche_avenant'),
    # path('affiche_avis', affiche_avis, name='affiche_avis'),
    # path('affiche_contrat', affiche_contrat, name='affiche_contrat'),
    # path('affiche_convention', affiche_convention, name='affiche_convention'),
    # path('affiche_lettreAccord', affiche_lettreAccord, name='affiche_lettreAccord'),
    # path('affiche_pds', affiche_pds, name='affiche_pds'),
    # path('affiche_st', affiche_st, name='affiche_st'),
    
    # path create
    path('accord_create', accord_create, name='accord_create'),
    path('accordOperation_create', accordOperation_create, name='accordOperation_create'),
    path('avenant_create', avenant_create, name='avenant_create'),
    path('avisJuridique_create', avisJuridique_create, name='avisJuridique_create'),
    path('contrat_create', contrat_create, name='contrat_create'),
    path('convention_create', convention_create, name='convention_create'),
    path('lettreAccord_create', lettreAccord_create, name='lettreAccord_create'),
    path('pds_create', pds_create, name='pds_create'),
    path('st_create', st_create, name='st_create'),

    # path update
    path('update_partenaire_fdup/<str:c>/', update_partenaire_fdup, name='update_partenaire_fdup'),
    path('update_accord/<str:c>/', update_accord, name='update_accord'),
    path('update_accordOp/<str:c>/', update_accordOp, name='update_accordOp'),
    path('update_avenant/<str:c>/', update_avenant, name='update_avenant'),
    path('update_avis/<str:c>/', update_avis, name='update_avis'),
    path('update_contrat/<str:c>/', update_contrat, name='update_contrat'),
    path('update_convention/<str:c>/', update_convention, name='update_convention'),
    path('update_lettreAccord/<str:c>/', update_lettreAccord, name='update_lettreAccord'),
    path('update_pds/<str:c>/', update_pds, name='update_pds'),
    path('update_st/<str:c>/', update_st, name='update_st'),
    path('update_user/<str:u>/', update_user, name="update_user"),

    # path delete
    path('delete_partenaire/<str:c>/', delete_partenaire, name='delete_partenaire'),
    path('delete_fdup/<str:c>/', delete_fdup, name='delete_fdup'),
    path('delete_accord/<str:c>/', delete_accord, name='delete_accord'),
    path('delete_accordOp/<str:c>/', delete_accordOp, name='delete_accordOp'),
    path('delete_avenant/<str:c>/', delete_avenant, name='delete_avenant'),
    path('delete_avis/<str:c>/', delete_avis, name='delete_avis'),
    path('delete_contrat/<str:c>/', delete_contrat, name='delete_contrat'),
    path('delete_convention/<str:c>/', delete_convention, name='delete_convention'),
    path('delete_lettreAccord/<str:c>/', delete_lettreAccord, name='delete_lettreAccord'),
    path('delete_pds/<str:c>/', delete_pds, name='delete_pds'),
    path('delete_st/<str:c>/', delete_st, name='delete_st'),
    path('delete_user/<str:u>/', delete_user, name="delete_user"),

    #path affiche_detail
    path('affiche_detail_accord/<str:c>/', affiche_detail_accord, name='affiche_detail_accord'),
    
    # history
    path('view_history', view_history, name='view_history'),

    # path('accounts/', include('django.contrib.auth.urls')),
    
    # reset password urls  
    path('password_change',PasswordsChangeView.as_view(template_name='mdp.html'), name="password_change"),
    
    path('password_reset',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name="password_reset"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
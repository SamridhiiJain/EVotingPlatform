from django.urls import path
from .import views


urlpatterns = [
    #login 
    
    path('', views.index , name='index'),

    #voter

    path('c/login', views.login_view , name='login'),
    path('c/register', views.register_view , name='register'),
     path('c/voter', views.voter_view , name='voter'),

     #candidate

    path('s/login', views.clogin_view , name='candidate_login'),
    path('s/register', views.cregister_view , name='candidate_register'),
    path('s/candidate', views.cadidate_view , name='candidate'),
    
    #party
    path('s/login', views.plogin_view , name='party_login'),
    path('s/register', views.pregister_view , name='party_register'),
    path('s/party', views.party_view , name='party'),

    #logout

    path('logout', views.logout_view , name='logout'),
]
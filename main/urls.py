from django.urls import path
from .import views


urlpatterns = [
    #login 
    
    path('', views.index , name='index'),
    
    #login

    path('/login', views.login , name='login'),

    #register
    # path('/register', views.register , name='register'),
 
    #choose the type of election

    path('choice/election/PGE', views.choice_PGE , name='PGE'),
    path('choice/election/SAE', views.choice_SAE , name='SAE'),

    #choose your constituency
    path('choice/constituency', views.choice_constituency_PGE , name='choice_PGE_constituency'),
    
    path('choice/constituency', views.choice_constituency_SAE , name='choice_SAE_constituency'),
    
    #Type of constituency
    path('choice/PGE/constituency', views.PGE_constituency , name='PGE_constituency'),
    path('choice/SAE/constituency', views.SAE_constituency , name='SAE_constituency'),

    #voter

    path('v/login', views.login_view , name='voter_login'),
    path('v/register', views.register_view , name='voter_register'),
     path('v/voter', views.voter_view , name='voter'),

     #candidate

    path('c/login', views.clogin_view , name='candidate_login'),
    path('c/register', views.cregister_view , name='candidate_register'),
    path('c/candidate', views.candidate_view , name='candidate'),
    
    #party

    path('p/login', views.plogin_view , name='party_login'),
    path('p/register', views.pregister_view , name='party_register'),
    path('p/party', views.party_view , name='party'),

    #logout

    path('logout', views.logout_view , name='logout'),
]
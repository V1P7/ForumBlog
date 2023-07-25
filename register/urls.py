from django.urls import path
from django.urls import path
from register import views as accounts_views

urlpatterns = [
    path('signup/', accounts_views.signup, name='signup'),
    path('signin/', accounts_views.signin, name='signin'),
    path('logout/', accounts_views.logout_view, name='logout'),
    path('update_profile/', accounts_views.update_profile, name='update_profile'),
]

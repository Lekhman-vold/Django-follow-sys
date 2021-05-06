from django.urls import path
from .views import profile, follow_toggle, profiles

urlpatterns = [
    path("profiles/", profiles, name="profiles"),
    path("profile/<str:username>/", profile, name='profile'),
    path("followToggle/<str:author>/", follow_toggle, name="followToggle"),
]

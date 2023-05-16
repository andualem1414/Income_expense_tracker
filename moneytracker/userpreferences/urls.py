from . import views
from django.urls import path


urlpatterns = [
    path('', views.UserPereferencesView.as_view(), name="preferences"),
]

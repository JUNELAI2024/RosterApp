from django.urls import path
from .views import index, view_roster, save_roster

urlpatterns = [
    path('', index, name='index'),  # Home page view
    path('roster/', view_roster, name='view_roster'),  # Roster view
    path('save_roster/', save_roster, name='save_roster'),  # Save roster view
]
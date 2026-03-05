from django.urls import path
from .views import dashboard_view, specification_view, implementation_guide_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('specification/', specification_view, name='specification'),
    path('implementation-guide/', implementation_guide_view, name='implementation_guide'),
]

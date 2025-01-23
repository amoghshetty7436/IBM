from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home_page, name='home'),
    path('eyes/', views.eyes_page, name='eyes'),
    path('nails/', views.nails_analysis, name='nails_page'),  # Updated to use nails_analysis view
    path('teeth/', views.teeth_page, name='teeth'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

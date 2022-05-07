from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('detectme', views.detectme, name='detectme'),
    path('', views.index, name='index'),
    path('<int:user_id>/', views.detail, name='detail'),
    path('management', views.management, name='management'),
    path('live', views.live, name='live'),
]
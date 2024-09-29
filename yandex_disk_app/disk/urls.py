from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('files/', views.file_list, name='file_list'),
    path('download/<path:file_path>/', views.download_file, name='download_file'),
    path('download_files/', views.download_files, name='download_files'),  # Для скачивания нескольких файлов
]
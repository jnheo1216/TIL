from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),  # R
    path('new/', views.new, name='new'),  # C
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),  # R

    # 여기까지
    path('<int:pk>/edit/', views.edit, name='edit'),  # U
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),  # D
]
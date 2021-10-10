from . import views
from  django.urls import path

urlpatterns = [
    path('adminlogin/',views.login,name='adminlogin'),
    path('addbook/', views.addbook, name='addbook'),
    path('showbook/',views.showbook, name='showbook'),
    path('delete/<book_id>/',views.delete,name='delete'),
]
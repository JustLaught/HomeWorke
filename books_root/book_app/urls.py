from django.urls import path
from . import views

app_name = 'book_app'
urlpatterns=[
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('writers/<str:name>/<str:book_name>/', views.writers, name='writers'),
    path('writers/<str:name>/', views.writers, name='writers'),
    path('writers/', views.writers, name='writers'),
    path('books/<str:name>', views.books, name='books'),
    path('books/', views.books, name='books'),
    path('contact/', views.contact, name='contact'),
]
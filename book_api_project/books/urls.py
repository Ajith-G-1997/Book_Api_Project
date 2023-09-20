
from django.urls import path
from . import views
from .views import StoreListView,StoreListView

urlpatterns = [
    path('authors/', views.AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author-detail'),
    path('books/', views.BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
    #path('auth/',views.First.as_view(),name='auth'),
    path('bookstore/', StoreListView.as_view(), name='bookstore-list'),
    path('stores/', StoreListView.as_view(), name='store-list'),
]

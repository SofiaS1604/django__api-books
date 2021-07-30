from django.urls import path
from .views import BookView, AuthorView

app_name = 'book'
urlpatterns = [
    path('books/', BookView.as_view()),
    path('books/<int:pk>', BookView.as_view()),
    path('authors/', AuthorView.as_view()),
    path('authors/<int:pk>', AuthorView.as_view())
]
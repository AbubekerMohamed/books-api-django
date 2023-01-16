from django.urls import path
from book_api.views import BookList, BookCreate, BookMutate
urlpatterns = [
    path('', BookCreate.as_view()),
    path("list/", BookList.as_view()),
    path("<int:pk>", BookMutate.as_view())
]

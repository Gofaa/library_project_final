from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import BookListApiView, book_list_View, BookDetailApiView, \
    BookDeleteApiView, BookUpdateApiView, BookListCreateApiView, BookCreateApiView, BookViewset

urlpatterns = [
    # path('',BookListApiView.as_view(),),
    # path('books/create/', BookCreateApiView.as_view()),
    # path('booklistcreate/',BookListCreateApiView.as_view()),
    # path('books/', book_list_View),
    # path('books/<int:pk>/', BookDetailApiView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view()),

]

router = SimpleRouter()
router.register('books', BookViewset, basename='books')
urlpatterns += router.urls
from rest_framework.routers import DefaultRouter

from book_manager.views import BookViewSet


router = DefaultRouter()
router.register('books', BookViewSet, basename='books')

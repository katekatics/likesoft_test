from django.contrib import admin
from django.urls import path, include

from books.routers import DefaultRouter
from book_manager.urls import router as book_manager_router
from users.urls import router as users_router

router = DefaultRouter()
router.extend(book_manager_router)
router.extend(users_router)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

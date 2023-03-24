from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from book.views import BookViewSet, AuthorViewSet

router = routers.DefaultRouter()
router.register(r'book', BookViewSet)
router.register(r'author', AuthorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api', include(router.urls)),
]

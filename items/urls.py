from django.urls import path, include
from rest_framework.routers import DefaultRouter

from items.views import ItemBasesViewset, RunesViewset, RunewordsViewset, ItemsViewset

router = DefaultRouter()
router.register(r'items', ItemsViewset, basename="items")
router.register(r'bases', ItemBasesViewset, basename="bases")
router.register(r'runes', RunesViewset, basename="runes")
router.register(r'runewords', RunewordsViewset, basename="runewords")

urlpatterns = [
    path('api/', include((router.urls, "items")))
]

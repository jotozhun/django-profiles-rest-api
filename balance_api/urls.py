from django.urls import path, include
from rest_framework.routers import DefaultRouter
from balance_api import views

router = DefaultRouter()
router.register('balance', views.BankAccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

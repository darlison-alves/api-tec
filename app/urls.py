from django.urls import path, include
from . import views 
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('montagem', views.MontagemView)
router.register('placas-mae', views.PlacaMaeView)
router.register('processadores', views.ProcessadorView)

urlpatterns = [
    path('', include(router.urls))
]

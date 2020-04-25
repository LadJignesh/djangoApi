from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('challenges', views.ChallengeView)
router.register('challengesData', views.ChallengeDataView)

urlpatterns = [
    path('', include(router.urls))
]
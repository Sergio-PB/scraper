from django.urls import path, include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('subject', views.subjectView)
router.register('author', views.authorView)
router.register('article', views.articleView)

urlpatterns = [
    path('', views.index, name='index'),
    path('/api/', include(router.urls))
]

# urls.py
from rest_framework.routers import DefaultRouter
from chat.views import GroupMembershipViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'group-memberships', GroupMembershipViewSet)

urlpatterns = [
    # ... Your existing API endpoints ...
    path('api/', include(router.urls)),
]

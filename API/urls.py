from rest_framework.routers import DefaultRouter
from API.views import (
    UserViewSet,
    ProfilingInformationsViewSet,
    KKAddressViewSet,
    YouthStatusViewSet,
    EventViewSet
)

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='user')
router.register(r'profiling-informations', ProfilingInformationsViewSet, basename='profiling-informations')
router.register(r'kk-addresses', KKAddressViewSet, basename='kk-address')
router.register(r'youth-statuses', YouthStatusViewSet, basename='youth-status')
router.register(r'events', EventViewSet, basename='event')

urlpatterns = router.urls
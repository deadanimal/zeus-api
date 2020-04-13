
from datetime import datetime, timedelta

from django.conf import settings
from django.conf.urls import include, url
from django.contrib.gis import admin

from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


from users.views import (
    MyTokenObtainPairView
)

from organisations.views import (
    OrganisationViewSet,
)

from users.views import (
    CustomUserViewSet
)



class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass



router = NestedDefaultRouter()

organisations_router = router.register(
    'organisations', OrganisationViewSet
)

"""
organisation_types_router = router.register(
    'organisation-types', OrganisationTypeViewSet
)
"""

users_router = router.register(
    'users', CustomUserViewSet
)






urlpatterns = [

    url(r'v1/', include(router.urls)),
    url(r'auth/', include('rest_auth.urls')),
    url(r'auth/registration/', include('rest_auth.registration.urls')),

    url('auth/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    url('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),




]
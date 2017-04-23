from django.conf.urls import include, url
from material.frontend import urls as frontend_urls

urlpatterns = [
    url(r'^restaurant/', include('restaurant.urls')),
    url(r'', include(frontend_urls)),
]

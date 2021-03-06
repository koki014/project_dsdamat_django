"""damat_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import debug_toolbar
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import JavaScriptCatalog
from rest_framework.authtoken import views


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')), #Django translations URLS
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('api/v1.0/', include('product.api.urls', namespace='product_apis')),
    path('api/v1.0/', include('order.api.urls', namespace='order_apis')),
    path('api-auth/v1.0/', views.obtain_auth_token),
    path('api-auth/v1.0/', include('index.api.urls', namespace='index_apis')),
]


urlpatterns += i18n_patterns(
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('', include('index.urls', namespace='index')),
    path('product/', include('product.urls', namespace='product')),
    path('order/', include('order.urls', namespace='order')),
    path('account/', include('account.urls', namespace='account')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('__debug__/', include(debug_toolbar.urls)),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
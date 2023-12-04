from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from Core.views.common_views import example, health_test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health_test/', health_test),
    path('', example),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEV:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))

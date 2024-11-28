from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.http import JsonResponse


def hello_world(request):
    return JsonResponse({"hello": "world"})


urlpatterns = [
    path('', hello_world, name="hello_world"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

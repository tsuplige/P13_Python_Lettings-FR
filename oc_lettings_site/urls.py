from django.contrib import admin
from django.urls import path, include
from . import views


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('', views.index, name='index'),
    path('lettings/', include("lettings.urls")),
    path('profiles/', include("profiles.urls")),
    path('admin/', admin.site.urls),
]

handler404 = 'oc_lettings_site.views.error_404'
handler500 = 'oc_lettings_site.views.error_500'

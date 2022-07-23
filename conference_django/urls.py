from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # core urls
    path('', include('core.urls')),
    path('contact/', views.contact, name='contact'),

    # conference urls
    path('conference/', include('conference.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

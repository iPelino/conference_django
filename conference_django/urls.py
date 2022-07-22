from django.contrib import admin
from django.urls import path, include

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # core urls
    path('', include('core.urls')),
    path('contact/', views.contact),

    # conference urls
     path('conference/', include('conference.urls'))
]

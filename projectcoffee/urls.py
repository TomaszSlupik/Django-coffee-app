from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from coffee.views import all_coffee
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('coffee/', all_coffee)
] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



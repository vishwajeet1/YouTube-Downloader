from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index,download

urlpatterns = [
    path('',index,name="index"),
    path('download',download,name="download"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

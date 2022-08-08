from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static

from . import views

urlpatterns = [
    path('', views.manage_items, name="items"),
    path('<slug:key>', views.manage_item, name="single_item")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
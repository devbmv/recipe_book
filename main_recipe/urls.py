from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('recipe_book.urls'), name="blog-urls"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

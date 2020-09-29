from django.contrib import admin
from django.urls import path
import blogapp.views
from django.conf.urls import include # Add
from django.conf import settings # Add
from django.conf.urls.static import static # Add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.index, name='index'),
    path('blogMain/', blogapp.views.blogMain, name='blogMain'),
    path('blogMain/createBlog/', blogapp.views.createBlog, name='createBlog'),
    path('ckeditor/', include('ckeditor_uploader.urls')), # Add
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Add
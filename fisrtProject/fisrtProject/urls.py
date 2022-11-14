from . import views
from . import coba
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('coba/', coba.Testing),
    path('admin/', admin.site.urls),
    path('kontak/', views.contact, name='contact')
]

urlpatterns += staticfiles_urlpatterns()

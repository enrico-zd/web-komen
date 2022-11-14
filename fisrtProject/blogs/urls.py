from . import views
from django.urls import path

app_name = 'blogs' # untuk namespace

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.single, name='single'),
    path('blogs/<int:id>', views.comment, name='comment'),
]

hander404 = 'views.handler404'

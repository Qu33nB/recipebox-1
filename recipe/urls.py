from django.urls import path

from recipe import views


urlpatterns = [
    path('', views.index),
    path('', views.author),
    path('', views.recipe),
    # path('author/<int:id>/', views.author)
    # path('admin/', admin.site.urls),
]

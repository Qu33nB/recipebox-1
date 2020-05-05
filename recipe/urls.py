from django.urls import path

from recipe import views


urlpatterns = [
    path('', views.index),
    path('', views.author),
    path('', views.recipe),
    # path('addrecipe/', views.addrecipe),
    # path('author/<int:id>/', views.author)
    # path('admin/', admin.site.urls),
]

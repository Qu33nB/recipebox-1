from django.urls import path

from recipe import views


urlpatterns = [
    path('author/<int:id>/', views.author, name='author_url'),
    path('recipe/<int:id>/', views.recipe, name='recipe_url'),
    path('home/', views.index, name='homepage'),
    path('addrecipe/', views.addrecipe, name='addrecipe'),
    path('addauthor/', views.addauthor, name='addauthor'),
    path('login/', views.loginview, name='login_url'),
    path('logout/', views.logoutview, name='logout_url'),
    path('editrecipe/', views.edit_recipe, name='edit'),
    path('add_fave/<int:id>/', views.add_favorite, name='fave'),
    path('remove_fave/<int:id>/', views.remove_favorite, name='unfave')
]

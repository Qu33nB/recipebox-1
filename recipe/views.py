from django.shortcuts import render

from recipe.models import Author, RecipeItem

# Create your views here.


def index(request):
    data = RecipeItem.objects.all()
    return render(request, 'index.html', {'data': data})


def author(request, id):
    author = Author.objects.get(id=id)
    recipe = RecipeItem.objects.filter(author=author)
    data = RecipeItem.objects.all()
    return render(request, 'author.html', {
        'author': author, 'recipe': recipe, 'data': data
    })
    # data = RecipeItem.objects.filter(author__id=id)
    # return render(request, 'author.html', {'data': data})


def recipe(request, id):
    recipe = RecipeItem.objects.get(id=id)

    return render(request, 'recipe.html', {'recipe': recipe})

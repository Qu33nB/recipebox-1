from django.shortcuts import render, reverse, HttpResponseRedirect

from recipe.models import Author, RecipeItem
from recipe.forms import AddRecipeForm, AddAuthorForm
# Create your views here.


def index(request):
    data = RecipeItem.objects.all()
    return render(request, 'index.html', {'data': data})


def addrecipe(request):
    html = "addrecipeform.html"

    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            RecipeItem.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                time_required=data['time_required'],
                instruction=data['instruction']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddRecipeForm()

    return render(request, html, {"form": form})


def addauthor(request):
    html = "addauthorform.html"

    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AddAuthorForm()

    return render(request, html, {'form': form})


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

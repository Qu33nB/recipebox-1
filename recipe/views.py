from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from recipe.models import Author, RecipeItem
from recipe.forms import AddRecipeForm, AddAuthorForm, LoginForm
from django.contrib.auth.models import User
# Create your views here.


def logoutview(request):
    if logout(request):
        return HttpResponseRedirect(reverse('homepage'))
    return render(request, 'logoutpage.html', {})


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'genericform.html', {'form': form})


def index(request):
    data = RecipeItem.objects.all()
    return render(request, 'index.html', {'data': data})


@login_required
def addrecipe(request):
    html = "genericform.html"

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


@login_required
def addauthor(request):
    html = "genericform.html"
    form = AddAuthorForm()

    if request.method == "POST":
        form = AddAuthorForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(
                username=data['name']
            )
            # With a lot of help from Koren, was able to get author add working
            new_author = Author.objects.create(
                name=data['name'], bio=data['bio'], user=new_user)
            new_author.save()
            return HttpResponseRedirect(reverse('homepage'))

    if request.user.is_staff:

        return render(request, html, {"form": form})

    return render(request, 'forbidden.html')


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

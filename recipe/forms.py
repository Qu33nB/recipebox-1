from django import forms
from recipe.models import Author, RecipeItem
# class AddAuthorForm


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=30)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=30)
    instruction = forms.CharField(widget=forms.Textarea)


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'name', 'bio'
        ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class EditRecipeForm(forms.ModelForm):
    
    class Meta:
        model = RecipeItem
        fields = [
            'title',
            'author',
            'description',
            'time_required',
            'instruction',
        ]

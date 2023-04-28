from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from .models import Recipe
from django.core.cache import cache
# Create your views here.

class RecipesView(ListView):
    queryset = Recipe.objects.all()
    context_object_name = "recipes"
    template_name = "recipe/recipes.html"

class RecipeView(View):
    template_name = "recipe/recipe.html"
    def get(self, request, *args, **kwargs):
        recipe_id = kwargs["pk"]
        if cache.get(recipe_id):
            recipe = cache.get(recipe_id)
            print("hit the cache")
        else:
            recipe = get_object_or_404(Recipe, pk=recipe_id)
            cache.set(recipe_id,recipe)
            print("hit the db")
        return HttpResponse("Detail Page")
        context = {"recipe": recipe}
        return render(request, self.template_name, context)

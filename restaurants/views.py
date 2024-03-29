from django.http import Http404
from django.views.generic import DetailView, ListView, TemplateView
from django.utils.translation import gettext_lazy as _

from .models import Restaurant, Food, Category


class IndexView(TemplateView):
    template_name = 'restaurants/index.html'


class AboutView(TemplateView):
    template_name = 'restaurants/about.html'


class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurants/restaurant_list.html'
    context_object_name = 'restaurants'


class FoodRestaurantListView(ListView):
    model = Food
    template_name = 'restaurants/restaurant_foods.html'
    context_object_name = 'foods'

    def get_queryset(self):
        food = Food.objects.filter(restaurant__slug=self.kwargs.get('slug'))
        food_by_category = food.filter(category=self.kwargs.get('category__id'))
        if self.kwargs.get('category__id'):
            return food_by_category
        return food

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(food__restaurant__slug=self.kwargs.get('slug')).distinct()

        return context


class FoodDetailView(DetailView):
    model = Food
    template_name = 'restaurants/food_detail.html'
    context_object_name = 'food_detail'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        restaurant_slug = self.kwargs.get('restaurant_slug', None)
        food_slug = self.kwargs.get('food_slug', None)
        try:
            obj = queryset.get(slug=food_slug, restaurant__slug=restaurant_slug)
        except queryset.model.DoesNotExist:
            raise Http404(_("Nie znaleziono takiego posiłku"))
        return obj

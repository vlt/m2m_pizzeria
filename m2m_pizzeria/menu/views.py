from django.views.generic import ListView, UpdateView

from menu.models import Pizza


class PizzaListView(ListView):
    model = Pizza


class PizzaUpdateView(UpdateView):
    model = Pizza
    fields = ["toppings"]

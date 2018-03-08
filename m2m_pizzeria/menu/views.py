from django.views.generic import ListView, UpdateView

from menu.forms import PizzaForm
from menu.models import Pizza


class PizzaListView(ListView):
    model = Pizza


class PizzaUpdateView(UpdateView):
    model = Pizza
    form_class = PizzaForm

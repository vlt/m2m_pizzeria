from django import forms

from .models import Pizza, ToppingOnPizza


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ["toppings"]

    def save(self, commit=True):
        pizza = super().save(commit=False)

        if commit:
            pizza.save()

            if "toppings" in self.changed_data:
                final_toppings = self.cleaned_data["toppings"]

                ToppingOnPizza.objects.filter(
                    pizza=pizza,
                ).exclude(
                    topping__in=final_toppings,
                ).delete()

                initial_toppings = self.initial.get("toppings", {})
                toppings_to_add = (
                    topping for topping in final_toppings
                    if topping not in initial_toppings
                )
                for topping in toppings_to_add:
                    ToppingOnPizza.objects.create(pizza=pizza, topping=topping)

        return pizza

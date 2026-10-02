from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home_page_view(request):
    context = { 
        "inventory": ["Treasure Chest", "Sword", "Armour"],
        "greeting": "Look upon our inventory!"
    }
    return render(request, "home.html", context)

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "Your Local Mountain Cave"
        context["phone_number"] = "790-955-916-0"
        return context

class ProductsPageView(TemplateView):
    template_name = "products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["helmet"] = "Iron Helmet ~ $25"
        context["robe"] = "Magic Robe ~ $75"
        context["sword"] = "Shiny Sword ~ $125"
        context["sweet_roll"] = "Sweet Roll ~ $2" 
        return context

    
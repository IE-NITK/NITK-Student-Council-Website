from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"

class represent(generic.TemplateView):
    template_name = "represent.html"

from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"

class clublife(generic.TemplateView):
    template_name = "clublife.html"

class represent(generic.TemplateView):
    template_name = "represent.html"
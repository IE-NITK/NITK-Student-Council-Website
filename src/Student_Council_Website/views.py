from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"

class RepresentPage(generic.TemplateView):
    template_name = "represent.html"

class AboutPage(generic.TemplateView):
    template_name = "about.html"

class MessagePage(generic.TemplateView):
	template_name = "message.html"

class ClubLifePage(generic.TemplateView):
	template_name = "clublife.html"

class NitkLifePage(generic.TemplateView):
	template_name = "nitk_life.html"
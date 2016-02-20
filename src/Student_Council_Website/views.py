from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"

class represent(generic.TemplateView):
    template_name = "represent.html"

class AboutPage(generic.TemplateView):
    template_name = "about.html"

class MessagePage(generic.TemplateView):
	template_name = "message.html"

class ClubLifePage(generic.TemplateView):
	template_name="clublife.html"

class FAQ(generic.TemplateView):
	template_name="faq.html"
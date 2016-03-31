from django.contrib import admin
from .models import *

# Register your models here.
class FilterEventsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.organizer = request.user.club
        obj.save()
    def get_queryset(self, request):
        qs = super(FilterEventsAdmin, self).get_queryset(request)
        return qs.filter(organizer=request.user.club)

class EventsAdmin(FilterEventsAdmin):
    fields = ['title','details','start','end','contact']

admin.site.register(Events,EventsAdmin)
admin.site.register(Club)
admin.site.register(News)
admin.site.register(Articles)
admin.site.register(Member)
admin.site.register(Author)
admin.site.register(Complaint)
admin.site.register(Announcements)

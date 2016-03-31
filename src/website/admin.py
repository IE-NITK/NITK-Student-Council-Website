from django.contrib import admin
from .models import *

# Register your models here.
class FilterEventsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.organizer = request.user.club
        obj.save()
    def get_queryset(self, request):
        qs = super(FilterEventsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(organizer = request.user.club)
    def has_change_permission(self, request, obj=None):
        if not obj:
            return True # So they can see the change list page
        if request.user.is_superuser or obj.organizer == request.user.club:
            return True
        else:
            return False
    has_delete_permission = has_change_permission

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
admin.site.register(Minute)
admin.site.register(ResearchGrant)
admin.site.register(MoU)
admin.site.register(Resource)
admin.site.register(SenateReport)

from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from contacts.models import Outbox, Inbox
from users_management.models import User


csrf_protected_method = method_decorator(csrf_protect)


@admin.register(Outbox)
class OutboxAdmin(admin.ModelAdmin):

    change_form_template = 'outbox/change_outbox.html'

    exclude = ['sender',]
    fields = ('receivers', 'subject', 'message',)
    list_display = ('subject', 'receivers_list', 'date',)

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False
        })
        return super().render_change_form(request, context, add=add, change=change, form_url=form_url, obj=obj)

    def get_queryset(self, request):
        qs = Outbox.objects.filter(sender=request.user)
        return qs

    def receivers_list(self, obj):
        outbox = Outbox.objects.get(id=obj.id)
        receivers = ''
        for receiver in outbox.receivers.all():
            receivers += receiver.username + '; '
        return receivers

    @csrf_protected_method
    def has_change_permission(self, request, obj=None):
        return False
    
    @csrf_protected_method
    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        obj.sender = request.user
        super().save_model(request, obj, form, change)
        outbox = Outbox.objects.get(id=obj.id)
        inbx = Inbox(outbox=outbox)
        inbx.save()


@admin.register(Inbox)
class InboxAdmin(admin.ModelAdmin):
    fields = [
        'sender',
        'receivers_list',
        'date',
        'subject',
        'message',
    ]

    list_display = ('subject', 'sender', 'date',)

    def get_queryset(self, request):
        qs = Inbox.objects.filter(outbox__receivers__id=request.user.id)
        return qs

    def sender(self, obj):
        outbox = Outbox.objects.get(id=obj.outbox.id)
        return outbox.sender.username

    def receivers_list(self, obj):
        outbox = Outbox.objects.get(id=obj.outbox.id)
        receivers = ''
        for receiver in outbox.receivers.all():
            receivers += receiver.username + '; '
        return receivers

    def date(self, obj):
        outbox = Outbox.objects.get(id=obj.outbox.id)
        return outbox.date

    def subject(self, obj):
        outbox = Outbox.objects.get(id=obj.outbox.id)
        return outbox.subject.name
    
    def message(self, obj):
        outbox = Outbox.objects.get(id=obj.outbox.id)
        return outbox.message

    @csrf_protected_method
    def has_add_permission(self, request):
        return False

    @csrf_protected_method
    def has_change_permission(self, request, obj=None):
        return False

    @csrf_protected_method
    def has_delete_permission(self, request, obj=None):
        return False

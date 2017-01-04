from django.shortcuts import render
from .models import Contact
from django.forms import ModelForm
from django.views import View
from django.forms import TextInput
from django.views.generic.edit import CreateView
from django.http import JsonResponse


class AjaxableResponseMixin(object):
    def form_invalid(self, form):
        print self.request.POST
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response
class ContactView(AjaxableResponseMixin, CreateView):
    model = Contact
    fields = ['name', 'email', 'phonenumber', 'message']
    template_name = 'contactme/contact.html'
    success_url = '/contact/'

    def form_valid(self, form):
        return super(ContactView, self).form_valid(form)

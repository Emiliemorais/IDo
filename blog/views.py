# -*- coding: utf-8 -*- 
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from django.utils.translation import ugettext, ugettext_lazy as _

from models import Message, Questionnaire
from manager.models import Enterprise
from forms import MessageForm, QuestionnarieForm

def home(request):
    return render(request, "home.html", {"Hello, world" : "You're at the polls index."})

class BudgetView(View):

    # Allowed methods on the view
    http_method_names = [u'get', u'post']

    template_name = 'budget.html'
    form = QuestionnarieForm

    context = {
        'form': form,
        'title': 'Budget Questionnarie',
    }
    
    def get(self, request):

        response = render(request, self.template_name, self.context) 
    
        return response

    def post(self, request):

        try:
            form = self.form(data=request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, _('Orcamento solicitado com sucesso. Entraremos em contato em breve.'))
                response = redirect('/') 
            else:
                self.context['form'] = form
                messages.add_message(request, messages.ERROR, _('Nao foi possivel solicitar o orcamento. Tente novamente.'))
                response = render(request, self.template_name, self.context) 
        except Exception as e:
            response = HttpResponse(str(e))

        return response


class MessageView(View):

    # Allowed methods on the view
    http_method_names = [u'get', u'post']

    template_name = 'contacts.html'
    enterprise = Enterprise.objects.get(id=1)
    success_view = 'contacts'
    form = MessageForm

    context = {
        'form': form,
        'title': 'Message',
        'enterprise' : enterprise
    }
    
    def get(self, request):
        try:
            response = render(request, self.template_name, self.context) 
        except Exception as e:
            response = HttpResponse(str(e))

        return response

    def post(self, request):

        try:
            form = self.form(data=request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, _('Mensagem enviada com sucesso. Entraremos em contato em breve.'))
                response = redirect(self.success_view)
            else:
                messages.add_message(request, messages.ERROR, _('Nao foi possivel enviar a mensagem. Tente novamente.'))
                response = render(request, self.template_name, self.context) 
        except Exception as e:
            response = HttpResponse(str(e))

        return response
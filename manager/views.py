# -*- coding: utf-8 -*- 
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib import messages
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from models import Enterprise
from forms import EnterpriseUpdateForm
from blog.models import Message, Questionnaire
from notifications.models import Notification

def index(request):
    enterprise = Enterprise.objects.get(id=1)
    return render(request, "manager_home.html", {'enterprise': enterprise})

class UpdateEnterpriseView(View):

    # Allowed methods on the view
    http_method_names = [u'get', u'post']

    template_name = 'update.html'
    enterprise = Enterprise.objects.get(id=1)
    success_view = 'index'
    form = EnterpriseUpdateForm

    context = {
        'title': 'Update Enterprise',
        'enterprise': enterprise
    }

    @method_decorator(login_required)
    def get(self, request, enterprise_id=None):

        context_form = self.form(instance=self.enterprise)
        try:
            self.context['form'] = context_form
            response = render(request, self.template_name, self.context) 
        except Exception as e:
            response = HttpResponse(str(e))

        return response

    @method_decorator(login_required)
    def post(self, request, enterprise_id=None):

        try:
            form = self.form(data=request.POST, instance=self.enterprise)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, _(u'Informações atualizadas com sucesso.'))
                response = redirect(self.success_view)
            else:
                self.context['form'] = form
                messages.add_message(request, messages.ERROR, _('Nao foi possivel atualizar as informacoes'))
                response = render(request, self.template_name, self.context) 
        except Exception as e:
            response = HttpResponse(str(e))

        return response

class MessageView(View):

    # Allowed methods on the view
    http_method_names = [u'get', u'post']

    template_name = 'messages.html'

    def get_all_messages(self):
        visitant_messages = Message.objects.all()
        context = {
            'visitant_messages' : visitant_messages
        }
       
        return context

    @method_decorator(login_required)
    def get(self, request):
        try:
            context = self.get_all_messages()
            # When see messages, mark notifications as read
            self.mark_messages_notifications_as_read()
            response = render(request, self.template_name, context) 
        except Exception as e:
            response = HttpResponse(str(e))

        return response

    @method_decorator(login_required)
    def post(self, request, message_id=None):
        try:
            message = Message.objects.get(id=message_id)
            message.delete()
            context = self.get_all_messages()
            messages.add_message(request, messages.SUCCESS, _('Mensagem excluida com sucesso.')) 
            response = render(request, self.template_name, context) 
        except Exception as e:
            response = HttpResponse(str(e))

        return response

    def mark_messages_notifications_as_read(self):
        notifications = Notification.objects.filter(verb="send a new message")
        for notification in notifications:
            notification.mark_as_read()


class BudgetView(View):

    # Allowed methods on the view
    http_method_names = [u'get', u'post']

    template_name = 'budgets.html'

    def get_all_solicited_budgets(self):
        budgets = Questionnaire.objects.all()
        context = {
            'budgets' : budgets
        }
       
        return context

    @method_decorator(login_required)  
    def get(self, request, budget_id=None):

        context = self.get_all_solicited_budgets()
        response = render(request, self.template_name, context) 
        
        return response

    @method_decorator(login_required)  
    def show_budget(self, request, budget_id=None):

        budget = Questionnaire.objects.get(id=budget_id)
        context = {
            'budget' : budget
        }
        response = render(request, 'show_budget.html', context) 
    
        return response

    @method_decorator(login_required)  
    def post(self, request, budget_id=None):

        try:
            budget = Questionnaire.objects.get(id=budget_id)
            budget.delete()
            context = self.get_all_solicited_budgets()
            messages.add_message(request, messages.SUCCESS, _('Pedido de orcamento excluido com sucesso.')) 
            response = render(request, self.template_name, context) 
        except Exception as e:
            response = HttpResponse(str(e))

        return response
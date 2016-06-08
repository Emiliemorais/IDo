from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse

from models import Message
from manager.models import Enterprise
from forms import MessageForm

def home(request):
	return render(request, "home.html", {"Hello, world" : "You're at the polls index."})

class BudgetView(View):

    # Allowed methods on the view
    http_method_names = [u'get', u'post']

    template_name = 'budget.html'

    def get(self, request):

       	context = {}
        response = render(request, self.template_name, context) 
    
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
                response = redirect(self.success_view)
            else:
                response = render(request, self.template_name, self.context) 
        except Exception as e:
            response = HttpResponse(str(e))

        return response

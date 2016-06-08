from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View

from models import Enterprise
from forms import EnterpriseUpdateForm

def index(request):
    enterprise = Enterprise.objects.get(id=1)
    return render(request, "home.html", {'enterprise': enterprise})

def about(request):
    enterprise = Enterprise.objects.get(id=1)
    return render(request, "about.html", {'enterprise': enterprise.who})


def address(request):
    enterprise = Enterprise.objects.get(id=1)
    return render(request, "address.html", {'enterprise': enterprise.address})

class UpdateEnterpriseView(View):

    # Allowed methods on the view
    http_method_names = [u'get', u'post']

    template_name = 'update.html'
    enterprise = Enterprise.objects.get(id=1)
    success_view = 'index'
    form = EnterpriseUpdateForm

    def get(self, request, enterprise_id=None):

        context_form = self.form(instance=self.enterprise)

        try:
            context = {
                'form': context_form,
                'title': 'Update Enterprise',
                'enterprise': self.enterprise
            }

            response = render(request, self.template_name, context) 
        except Exception as e:
            response = HttpResponse(str(e))

        return response

    def post(self, request, enterprise_id=None):

        try:
            form = self.form(data=request.POST, instance=self.enterprise)
            if form.is_valid():
                form.save()
                response = redirect(self.success_view)
            else:
                self.context_form = form
                context = {
                    'form': context_form,
                    'title': 'Update Enterprise',
                    'enterprise': self.enterprise
                }
                response = render(request, self.template_name, context) 
        except Exception as e:
            response = HttpResponse(str(e))

        return response

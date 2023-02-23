from django.shortcuts import render

# Create your views here.


def home(request, *args, **kwargs):
    return render(request, 'base.html')

from django.shortcuts import render
from django.views import View
from .models import * 
from django.contrib import messages

from django.http import HttpResponse



import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.template.loader import get_template

from django.db import transaction





from django.utils.translation import gettext as _


# Create your views here.

class HomeView( View):
    """ Main view """

    templates_name = 'index.html'

    invoices = Invoice.objects.select_related('customer', 'save_by').all().order_by('-invoice_date_time')

    context = {
        'invoices': invoices
    }

    def get(self, request, *args, **kwags):
        
        return render(request, self.templates_name, self.context)


    def post(self, request, *args, **kwagrs):
        
        return render(request, self.templates_name, self.context)    


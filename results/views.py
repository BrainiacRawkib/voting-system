from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from states.models import LGA, PollingUnit
from .models import AnnouncedLGAResult, AnnouncedPUResult


class IndexView(TemplateView):
    template_name = 'results/index.html'


class LGAResultListView(ListView):
    model = AnnouncedLGAResult
    template_name = 'results/lga_results.html'
    ordering = '-date'


    def get_context_data(self, *, object_list=None, **kwargs):        
        results = AnnouncedLGAResult.objects.all()
        context = {
            'title': 'LGA Results',
            'results': results,            
        }
        return context


class LGATotalResult(DetailView):
    model = PollingUnit
    template_name = 'results/summed_results.html'

    def get_context_data(self, **kwargs):
        pu_result = get_object_or_404(PollingUnit, self.kwargs.get('name'))        
        context = {
            'result': pu_result
        }
        return context
    


class PUResultListView(ListView):
    model = AnnouncedPUResult
    template_name = 'results/pu_results.html'
    ordering = '-date'

    def get_context_data(self, *, object_list=None, **kwargs):
        results = AnnouncedPUResult.objects.all()        
        context = {
            'title': 'PU Results',
            'results': results
        }
        return context

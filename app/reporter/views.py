from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse

from reporter.models import Incidence

class HomePageView(TemplateView):
    template_name = 'index.html'


def patients_dataset(request):
    patients = serialize('geojson', Incidence.objects.all())
    return HttpResponse(patients, content_type='json')

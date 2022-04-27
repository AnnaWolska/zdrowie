from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from health.models import Bloodpressure, Glucoses
# from django.template import loader
# from django.contrib.auth.models import AnonymousUser
# from health.forms import HealthForm
from django.utils import timezone

def health_view(request):
    bloodpressures = Bloodpressure.objects.all()
    glucoses = Glucoses.objects.all()



from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from health.models import Bloodpressure, Glucoses
from health.forms import GlucosForm, BloodpressureForm
# from django.template import loader
# from django.contrib.auth.models import AnonymousUser
# from health.forms import HealthForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required()
def health_view(request):
    bloodpressures = Bloodpressure.objects.filter(user=request.user)
    glucoses = Glucoses.objects.filter(user=request.user)
    context = {"bloodpressures": bloodpressures, "glucoses":glucoses}
    return render(request, "health.html", context)


def add_glucos(request):
    form = GlucosForm
    if request.method == "POST":
        form = GlucosForm(request.POST, request.FILES)
        # formset = AuthorFormSet(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            # for f in form.cleaned_data:
            #     if f:
            #         author, _ = Author.objects.get_or_create(**f)
            #         # if author not in instance.authors.all():
            #         #     instance.authors.add(author)
            # instance.save()
        return HttpResponseRedirect(reverse("health:heath_view"))
    else:
        form = GlucosForm()
    return (
        render(request, "add_glucos.html", {"form": form})
    )



def add_bloodpressure(request):
    form = BloodpressureForm
    if request.method == "POST":
        form = BloodpressureForm(request.POST, request.FILES)
        # formset = AuthorFormSet(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            # for f in form.cleaned_data:
            #     if f:
            #         author, _ = Author.objects.get_or_create(**f)
            #         # if author not in instance.authors.all():
            #         #     instance.authors.add(author)
            # instance.save()
        return HttpResponseRedirect(reverse("health:heath_view"))
    else:
        form = BloodpressureForm()
    return (
        render(request, "add_bloodpressure.html", {"form": form})
    )

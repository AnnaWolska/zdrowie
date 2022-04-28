from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML, ButtonHolder
from django import forms
from health.models import Glucoses, Bloodpressure
from dal import autocomplete
from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelectMultiple


class GlucosForm(forms.ModelForm):

    # author = forms.ModelChoiceField(queryset=Author.objects.all(), required=False)

    class Meta:
        model = Glucoses
        fields = "user", "result1", "comment"
        labels = {
            "użytkownik",
            "wynik",
            "komentarz"
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.from_method = 'post'
            self.helper.from_method = 'health:add_glucos'
            # to jest dwa razy metod i działa, nie ma action, o co chodzi?
            self.helper.layout = Layout(
                Fieldset(
                    "użytkownik",
                    "wynik",
                    "komentarz"
                ),
                ButtonHolder(
                    Submit('submit', 'Dodaj', css_class='btn btn-primary'),
                    css_class="d-flex justify-content-end"
                )
            )


class BloodpressureForm(forms.ModelForm):

    class Meta:
        model = Bloodpressure
        fields = "user", "result1", "result2", "comment"
        lebels = {
        "użytkownik",
        "wynik1",
        "wynik2"
        "komentarz"
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.from_method = 'post'
            self.helper.from_method = 'health:add_bloodpressure'
            # to jest dwa razy metod i działa, nie ma action, o co chodzi?
            self.helper.layout = Layout(
                Fieldset(
                    "użytkownik",
                    "wynik",
                    "komentarz"
                ),
                ButtonHolder(
                    Submit('submit', 'Dodaj', css_class='btn btn-primary'),
                    css_class="d-flex justify-content-end"
                )
            )
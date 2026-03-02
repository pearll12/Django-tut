from django import forms 
from .models import ChaiVariety

class ChaiVarietyForm(forms.Form):
    # one of the way is modelchoice field that queries in your existing form - and gets the choices which have dropdown 
    # if we had given character field -> box deta where we had input chars
    chai_variety = forms.ModelChoiceField(queryset=ChaiVariety.objects.all(), label ="chai_variety")
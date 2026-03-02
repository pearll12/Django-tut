from django.shortcuts import render
from .models import ChaiVariety,Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm

# Create your views here.

def all_models(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais})

def chai_description(request, chai_id): #pass chai_id to the urls as well
    # chai id se array laado object 
    # model jisse laana hai and saath m primary key you can have other filters as well
    chai = get_object_or_404(ChaiVariety, pk = chai_id)
    # it will look in the template and look for chai/chai_detail.html , also pass an object 
    return render(request, 'chai/chai_detail.html', {'chai': chai} )

def chai_stores(request):
    stores=None
    # once user has submitted the form
    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety'] # to check if 
            stores = Store.objects.filter(chai_varieties = chai_variety) # searches for chai_variety in chai varities
    else:
        form = ChaiVarietyForm()
        # basic form ChaiVariety m jo bhi form hai as it is pass on krdo
    return render(request, "chai/chai_stores.html", {'stores': stores , 'form': form})

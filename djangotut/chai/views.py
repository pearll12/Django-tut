from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

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

from django.shortcuts import render
from .models import Recepmodel,Query
# Create your views here.



# Create your views here.

def solution(request):
    recepmodel = Recepmodel.objects.all()
    query = Query.objects.all()

    return render(request, "solution/solution.html",  {'query':query,'recepmodel':recepmodel} )

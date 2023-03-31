from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubmitForm
from .utils import DataHandler

# Create your views here.
def form_init(request):
    form = SubmitForm()
    return render(request, 'params_input.html', {'form': form} )
    #return HttpResponse('Hello World!')

def submit_form(request):
    
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        
        if form.is_valid():
            # print(form.cleaned_data)
            handler = DataHandler()
            context = handler.plot_main(form.cleaned_data)
            context['form'] = form
            
            # Redirect to a success page
            return render(request, 'plot.html', context )
        else:
            return render(request, 'params_input.html', { 'form': form} )

from django.shortcuts import render
#pack urls views
from django.urls import reverse_lazy 
#import packages 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
import json
#llamar al modelo que se enlazo a la tabla de la BD 
from MSWE.models import empresa
from MSWE.forms import empresaform
#from .forms import MyBooleanForm
#pakcages list
from django.shortcuts import render,redirect,get_object_or_404
from django.shortcuts import get_object_or_404
##########################################  modules #####################################
def Empresa(request):  
        
        return render(request,'MSWE/EmpresaLista.html')
#create view
#another way to make views

#other form views
# Create your views here.
"""A View is a place where we put the “logic” of our application. 
It will ask for information from the model you created before 
and pass it to the template."""
class EmpresaList(ListView):
    model = empresa
    template_name = 'MSWE/EmpresaLista.html'

class EmpresaCreate(CreateView):
    model =  empresa
    form_class = empresaform
    template_name = 'MSWE/add_empresa.html'
    success_url = reverse_lazy('ver_empresa')
    
class EmpresaUpdate(UpdateView):
    model =  empresa
    form_class = empresaform
    template_name = 'MSWE/add_empresa.html'
    success_url = reverse_lazy('ver_empresa')
     
    def get_object(self, queryset=None):
        print(self.kwargs)  # Debugging
        EmpresaId = self.kwargs.get('EmpresaId')
        Empresa=empresa.objects.all()
        print(EmpresaId)
        if not EmpresaId:
            raise Http404("EmpresaId not provided")
        return get_object_or_404(Empresa, EmpresaId=EmpresaId)

class EmpresaDelete(DeleteView):
    model = empresa
    form_class = empresaform
    template_name = 'MSWE/eliminar_empresa.html'
    success_url = reverse_lazy('ver_empresa')
    def get_object(self, queryset=None):
        print(self.kwargs)  # Debugging
        EmpresaId = self.kwargs.get('EmpresaId')
        Empresa=empresa.objects.all()
        print(EmpresaId)
        if not EmpresaId:
            raise Http404("EmpresaId not provided")
        return get_object_or_404(Empresa, EmpresaId=EmpresaId)
    
    """ f """
    """def EmpresaCreate(request):
    if request.method == 'POST':
        form = empresaform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Empresalist')
    else:
        form = empresaform()
    return render(request, 'MSWE/add_empresa.html', {'form': form})
#List View
#def EmpresasDetail(request):
 #  empresas = empresa.objects.all()
  # return render(request, 'MSWE/EmpresaLista.html', {'empresas': empresas})
def EmpresaList(request):
    empresas=empresa.objects.all()
    #empresas = get_object_or_404(empresa, pk=pk)
    #empresas=empresas.objects.all()
    #empresass=empresa.objects.all()
    return render(request,'MSWE/EmpresaLista.html',{'empresas': empresas})


#update view
def EmpresaUpdate(request, pk):
    empresas = get_object_or_404(empresa, pk=pk)
    em=empresas.objects.all()
    if request.method == 'POST':
        form = empresaform(request.POST, instance=empresas)
        if form.is_valid():
            form.save()
            return redirect('EmpresaList', pk=empresas.pk)
    else:
        form = empresaform(instance=empresas)
    return render(request, 'MSWE/add_empresa.html', {'form': form})


#delete view
def EmpresaDelete(request, pk):
    empresas = get_object_or_404(empresa, pk=pk)
    if request.method == 'POST':
        empresas.delete()
        return redirect('EmpresaList')
    return render(request, 'MSWE/eliminar_empresa.html', {'empresas': empresas})
"""
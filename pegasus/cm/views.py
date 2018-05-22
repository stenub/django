from django.shortcuts import render
from .forms import KundeForm, VMForm, VMFormSet
from .models import VM

# Create your views here.

def dashboard(request):
    return render(request, 'cm/dashboard.html', {})

def kunden_liste(request):
    return render(request, 'cm/kunden_liste.html', {})

def kunde_neu(request):
    form = KundeForm()
    return render(request, 'cm/kunde_edit.html', {'form': form})

def vm_liste(request):
    return render(request, 'cm/vm_liste.html', {})

#def vm_neu(request):
#    form = VMForm()
#    return render(request, 'cm/vm_edit.html', {'form': form})

def vm_neu(request):
    form = VMForm()
    vm_formset = VMFormSet(instance=VM())
    return render(request, 'cm/vm_edit.html', {'form': form, 'vm_formset': vm_formset,})


def change_liste(request):
    return render(request, 'cm/change_liste.html', {})

def change_neu(request):
    return render(request, 'cm/change_edit.html', {'form': form})

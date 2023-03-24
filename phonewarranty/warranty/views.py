from django.shortcuts import render, get_object_or_404
from .models import Phone, Warranty

def phone_list(request):
    phones = Phone.objects.all()
    return render(request, 'phone_list.html', {'phones': phones})

def phone_detail(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    warranties = Warranty.objects.filter(phone=phone)
    return render(request, 'phone_detail.html', {'phone': phone, 'warranties': warranties})

def warranty_detail(request, pk):
    warranty = get_object_or_404(Warranty, pk=pk)
    return render(request, 'warranty_detail.html', {'warranty': warranty})

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

#tax rate variable
tax_rate = 0.15

def home(request):
    # This is your default view
    return render(request, 'home.html')

def calculate_tax(request, anyNumber):  # Change 'price' to 'anyNumber' to match the URL pattern
    # This view takes a price and calculates tax
    total_price = anyNumber + (anyNumber * tax_rate)
    context = {'total_price': total_price}
    return render(request, 'calculate_tax.html', context)

def show_tax_rate(request):
    # This view just displays the tax rate
    context = {'tax_rate': tax_rate}
    return render(request, 'tax_rate.html', context)
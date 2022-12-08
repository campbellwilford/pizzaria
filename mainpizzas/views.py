from django.shortcuts import render, redirect 
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'mainpizzas/index.html')


def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')

    context = {'all_pizzas':pizzas}

    return render(request, 'mainpizzas/pizzas.html')


def pizza(request, pizza_id):
    p = Pizza.objects.get(id=pizza_id)

    toppings = Toppings.objects.filter(pizza=p)

    context = {'pizza':p, 'toppings':toppings}

    return render(request, 'mainpizzas/pizza.html')



def new_toppings(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = ToppingsForm()
    else:
        print(request.POST)
        form = ToppingsForm(data=request.POST)
        if form.is_valid():
            new_toppings = form.save(commit=False)
            new_toppings.pizza = pizza
            new_toppings.save()
            
            return redirect('mainpizza:pizza', pizza_id=pizza)

    context = {'form':form, 'pizza':pizza}

    return render(request, 'mainpizzas/new_pizza.html')
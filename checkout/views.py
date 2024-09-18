from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'sk_test_51Q0MMPRxTofVsr1TTwb26v30fBrjKxfqEcuMMkEoVtyDaEKu5nHEqQGXjEYpUieb4ay6ZzFnnKwPhY8yW1vrYLTH00pZp1pLdR',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
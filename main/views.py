from django.shortcuts import render
from . import models

def index(request):
    portfolio_items = models.PortfolioItem.objects.all()
    clients = models.Client.objects.all()

    content={
        'portfolio_items': portfolio_items,
        'clients': clients
    }

    return render(request, 'index.html', content)

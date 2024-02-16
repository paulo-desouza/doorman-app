from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from visitor.models import Visitor
from django.utils import timezone


@login_required     # ao utilizar este decorator, necessitas definir um redirect para ser feito o login, e outro para depois do login, em settings.py
def index(request):

    all_visitors = Visitor.objects.order_by(
        "-arrival_time"
    )

    awaiting_visitors = all_visitors.filter(
        status = "AWAITING"
    )

    in_visit_visitors = all_visitors.filter(
        status = "IN_VISIT"
    )

    finalized_visitors = all_visitors.filter(
        status = "FINALIZED"
    )
    
    current_month = timezone.now().month


    monthly_visitors = all_visitors.filter(
        arrival_time__month = current_month
    )


    context = {
        "nome_pagina": "Home",
        "all_visitors": all_visitors,
        "finalized_visitors" : finalized_visitors.count(),
        "in_visit_visitors" : in_visit_visitors.count(),
        "awaiting_visitors" : awaiting_visitors.count(),
        "monthly_visitors": monthly_visitors.count(),

    }

    return render(request, "index.html", context)




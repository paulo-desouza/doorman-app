from django.shortcuts import render
from visitor.models import Visitor


def index(request):

    all_visitors = Visitor.objects.all()



    context = {
        "nome_pagina": "Home",
        "all_visitors": all_visitors,
    }

    return render(request, "index.html", context)





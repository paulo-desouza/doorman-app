
from django.contrib import messages
from django.shortcuts import (
    render, redirect, get_object_or_404
)

from django.http import HttpResponseNotAllowed

from visitor.forms import (
    VisitorForm, AuthorizeVisitorForm
)
from visitor.models import Visitor


from django.utils import timezone


def register_visitor(request):   # THE REQUEST COMES FROM THE CLICK STRAIGHT INTO HERE DIRECTED FROM URLS.PY

    form = VisitorForm


    if request.method == "POST":
        form = VisitorForm(request.POST)

        if form.is_valid():
            visitor = form.save(commit = False)   # salvamos o formulario recebido no post, mas nao os enviamos ao banco de dados usando esse atributo.
                                                    # o formulario vem da classe VisitorsForm, que puxa o modelo Visitors para buildar o form em HTML
            
            visitor.registered_by = request.user.doorman    #request tem informacao a respeito do usuario e tambem variadas como OS 

            visitor.save()

            messages.success(
                request,
                "Visitor Successfully registered.",

            )

            return redirect("index")
 

    context = {
        "nome_pagina": "Register visitor",                   # context carrega as variaveis para o site
        "form": form,

    }

    return render(request, "register_visitor.html", context)




def information_visitor(request, id):

    visitor = get_object_or_404(
        Visitor,
        id=id,

    )

    form = AuthorizeVisitorForm()

    if request.method == "POST":
        form = AuthorizeVisitorForm(
            request.POST,
            instance = visitor
        )

        if form.is_valid():
            visitor = form.save(commit=False)

            visitor.status = "IN_VISIT"
            visitor.authorization_time = timezone.now()

            visitor.save()

            messages.success(
                request, 
                "Guest's entry successfully authorized"
            )

    context = {
        "nome_pagina": "Information visitor",
        "visitor": visitor,
        "form" : form,
    }


    return render(request, "information_visitor.html", context)


def finalize_visit(request, id):

    if request.method == "POST":

        visitor = get_object_or_404(
            Visitor,
            id=id
        )

        visitor.status = "FINALIZED"
        visitor.checkout_time = timezone.now()

        visitor.save()

        messages.success(
            request,
            "Visit successfully finalized"
        )

        return redirect("index")
    
    else:
        return HttpResponseNotAllowed(
            ["POST"],
            "Method not Allowed"
        )









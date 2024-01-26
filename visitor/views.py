
from django.contrib import messages
from django.shortcuts import (
    render, redirect, get_object_or_404
)


from visitor.forms import VisitorForm
from visitor.models import Visitor


def register_visitor(request):   # THE REQUEST COMES FROM THE CLICK STRAIGHT INTO HERE DIRECTED FROM URLS.PY

    form = VisitorForm


    if request.method == "POST":
        form = VisitorForm(request.POST)

        if form.is_valid():
            visitor = form.save(commit = False)   # salvamos o formulario recebido no post, mas nao os enviamos ao banco de dados usando esse atributo.
                                                    # o formulario vem da classe VisitorsForm, que puxa o modelo Visitors para buildar o form em HTML
            
            visitor.registrado_por = request.user.doorman    #request tem information a respeito do usuario e tambem variadas como OS 

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

    context = {
        "nome_pagina": "Information visitor",
        "visitor": visitor
    }


    return render(request, "information_visitor.html", context)






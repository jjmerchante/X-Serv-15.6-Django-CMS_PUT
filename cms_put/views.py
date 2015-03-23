from django.shortcuts import render
from models import Page
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden

# Create your views here.


@csrf_exempt
def mostrar(request, resource):
    if request.method == "GET":
        try:
            fila = Page.objects.get(name=resource)
            return HttpResponse(fila.page)
        except Page.DoesNotExist:
            return HttpResponseNotFound('Page not found: ' + resource)
        except Page.MultipleObjectsReturned:
            return HttpResponseNotFound('Server allocated more than \
                    one page for that resource')
    elif request.method == "PUT":
        newpage = Page(name=resource, page=request.body)
        newpage.save()
        return HttpResponse("New page added:\n" + request.body)
    else:
        return HttpResponseForbidden("Method not allowed")

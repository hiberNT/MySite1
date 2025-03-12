from django.http import HttpResponse #config do view no http configura o resultado que queremos mostrar no resultado final pro cliente que é a função do view inclusive
from django.views import generic #biblioteca do django


class PostView(generic.View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World')
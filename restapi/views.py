# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

class index(APIView):
    def get(self, request):
        message = "Hello, World!"
        return render(request, 'index.html', {'message': message})

def index(requests):
    return HttpResponse("Hello, world. You're at Rest.")

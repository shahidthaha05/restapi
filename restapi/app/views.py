from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializer import *
# Create your views here.


# def sample(req):
#     d={'name':'shahid','age';20}
#     return jsonresponse(d)


def user_def_serializer(req):
    if req.method=='GET':
        data=student.objects.all()
        d=user_serializer(data,many=True)
        return JsonResponse(d.data,safe=False)
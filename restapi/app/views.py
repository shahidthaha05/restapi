from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics,mixins
# Create your views here.


# def sample(req):
#     d={'name':'shahid','age';20}
#     return jsonresponse(d)


def user_def_serializer(req):
    if req.method=='GET':
        data=student.objects.all()
        d=user_serializer(data,many=True)
        return JsonResponse(d.data,safe=False)
    
@csrf_exempt
def fun1(req):
    if req.method=='GET':
        data=student.objects.all()
        d=model_serializer(data,many=True)
        return JsonResponse(d.data,safe=False)
    elif req.method=='POST':
        d=JSONParser().parse(req)
        data=model_serializer(data=d)
        if data.is_valid():
            data.save()
            return JsonResponse(data.data)
        else:
            return JsonResponse(data.errors)
        
def fun4(req,d):
    try:
        demo=student.objects.get(pk=d)
    except student.DoesNotExist:
        return HttpResponse('invalid')
    if req.method=='GET':
        s=model_serializer(demo)
        return JsonResponse(s.data)
    elif req.method=='PUT':
        d=JSONParser().parse(req)
        s=model_serializer(demo,data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors)
    elif req.method=='DELETE':
        demo.delete()
        return HttpResponse('deleted')
    

@api_view(['GET','POST'])
def fun5(req):
    if req.method=='GET':
        d=student.objects.all()
        s=model_serializer(d,many=True)
        return Response(s.data)
    elif req.method=='PSOT':
        s=model_serializer(data=req.data)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(s.errors,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def fun6(req,d):
    try:
        demo=student.objects.get(pk=d)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if req.method=='GET':
        s=model_serializer(demo)
        return Response(s.data)
    elif req.method=='PUT':
        s=model_serializer(demo,data=req.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif req.method=='DELETE':
        demo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class genericapiview(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class = model_serializer
    queryset = student.objects.all()
    def get(self,req):
        return self.list(req)
    def post(self,req):
        return self.create(req)
    

class update(generics.GenericAPIView,mixins.RetriviewModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = model_serializer
    queryset = student.objects.all()
    lookup_field = 'id'
    def get(self,req,id=None):
        return self.retrieve(req)
    def put(self,req,id=None):
        return self.update(req.id)
    def delete(self,req,id):
        return self.destroy(req,id)
    




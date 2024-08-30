from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from myapp.models import Cakes
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework import permissions,authentication
from  django.contrib.auth.models import User
from cakeapi.serializers import Userserializer


class Cakesserializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Cakes
        fields="__all__"
       # exclude=("id",)

class CakesView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Cakes.objects.all()
        if "flavour" in request.query_params:
            flavr=request.query_params.get("flavour")
            qs=qs.filter(flavour=flavr)

        if "shape" in request.query_params:
            shp=request.query_params.get("shape")
            qs=qs.filter(shape=shp)

        serializers=Cakesserializer(qs,many=True)
        return Response(data=serializers.data)
    
    def create(self,request,*args,**kwargs):
        serializer=Cakesserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Cakes.objects.get(id=id)
        serializer=Cakesserializer(qs)
        return Response(data=serializer.data)
    

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        emp_obj=Cakes.objects.get(id=id)
        serializer=Cakesserializer(instance=emp_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        try:
            Cakes.objects.get(id=id).delete()
            return Response(data="deleted")
        except Exception:
            return Response(data="no mataching record found")
        
    @action(methods=["get"],detail=False)
    def flavour(self,request,*args,**kwargs):
        qs=Cakes.objects.all().values_list("flavour",flat=True).distinct()
        return Response(data=qs)

    
class CakesViewsetView(ModelViewSet):
    serializer_class=Cakesserializer
    model=Cakes
    queryset=Cakes.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]


# serializer
class UsersView(ModelViewSet):
    serializer_class=Userserializer
    queryset=User.objects.all()
    model=User




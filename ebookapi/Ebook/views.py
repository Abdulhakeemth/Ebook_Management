from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import Ebooks,Rating
from .serializers import EbooksSerializer,UserRegister,RatingSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class RegisterView(APIView):
    def post(self,request,format=None):
        print(request.data)
        serializer=UserRegister(data=request.data)

        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registered'
            data['username']=account.username
            data['email']=account.email
            token,create=Token.objects.get_or_create(user=account)
            data['token']=token.key
        else:
            data=serializer.errors
        return Response(data)
class Ebooksdetiallist(APIView):   
    permission_classes = (IsAuthenticated,)


    def get(self, request, format=None):
        details = Ebooks.objects.all()
        serializer = EbooksSerializer(details,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EbooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class EbooksDetail(APIView):

    def get_object(self, pk):
        try:
            return Ebooks.objects.get(pk=pk)
        except Ebooks.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        details = self.get_object(pk)
        serializer = EbooksSerializer(details)
        return Response(serializer.data)

    def put(self, request,pk, format=None):
        book_data= self.get_object(pk)
        ebooks_serializer=EbooksSerializer(book_data,data=request.data)
        if ebooks_serializer.is_valid():
            ebooks_serializer.save()
            return Response(ebooks_serializer.data, status=status.HTTP_201_CREATED)
        return Response(ebooks_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk, format=None):
        book =  self.get_object(pk)
        book.delete()
        return Response("Deleted Successfully")
        return Response(status=status.HTTP_204_NO_CONTENT)
        


class Ratingdetaillist(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request,book,format=None):
        reviews = Rating.objects.filter(book= id)
        review_serializer = RatingSerializer(reviews) 
        sum = 0
        for i in reviews:
            sum = sum + i.Review
            avgrating=sum/len(reviews)
            bookdetails = {}
            bookdetails["details"] = review_serializer.data
            reviews["avgrating"] = avgrating
            return Response(bookdetails)




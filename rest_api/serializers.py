from django.shortcuts import redirect, render
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from buy_sell.models import NewUser
from buy_sell.models import Product
from buy_sell.models import Category

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}    

    def create(self, validated_data):
        user = NewUser.objects.create(
            username=validated_data['username'],
            name=validated_data['name'],
            email=validated_data['email'],
            phonenumber=validated_data['phonenumber'],
            password=validated_data['password'],
            
        )

        user.save()
        return user


class RegisteredUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = '__all__'
    


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        #fields = '__all__'
        #fields = ['ownerusername','owneremail','name','price','description','status']
        fields = ['id','ownerusername','owneremail','name','price','category','description']


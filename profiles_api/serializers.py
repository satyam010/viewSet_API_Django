from rest_framework import serializers



class HelloSerializer(serializers.Serializer):
	
	"""Serializes a name fields for testing our APIVIew"""
	name = serializers.CharField(max_length=10)
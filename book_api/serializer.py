from rest_framework import serializers
from django.forms import ValidationError

from book_api.models import Book

class BookSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = "__all__"

    def validate_title(self, value):
        if value == "Violate":
            raise ValidationError("No Violence")
        return value
    
    def validate(self, data):
        if data['number_of_pages'] > 200 and data['quantity'] > 200:
            raise ValidationError("To large to store")
        return data

    def get_description(self, data):
        return "This is book is titled "+ data.title
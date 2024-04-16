from rest_framework import serializers
from .models import NewsBD

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsBD
        fields = '__all__'
        # fields = [
        #     'pk', 'title', 'anons', 'content', 'date'
        # ]

class EmailSerializer(serializers.Serializer):
    recipient = serializers.EmailField()
    subject = serializers.CharField()
    content = serializers.CharField()
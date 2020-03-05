from rest_framework import  serializers
from .models import NewLeads

class NewLeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewLeads
        fields = '__all__'
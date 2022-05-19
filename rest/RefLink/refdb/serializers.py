from attr import field
from rest_framework import serializers

from refdb.models import RefDB

class RefDbSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    fullurl = serializers.CharField(required=False, allow_blank=True, max_length=250)
    shorturl = serializers.CharField(required=False, allow_blank=True, max_length=20)


class RefdbSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefDB
        field = ('id','fullurl','shorturl')

#     def create(self, validated_data):
#         return RefDB.objects.create(validated_data)

# def update(self, instance, validated_data):
#     instance.fullurl = validated_data.get('fullurl',instance.fullurl)
#     instance.shorturl = validated_data.get('shorturl',instance.shorturl)
#     instance.save()
#     return instance
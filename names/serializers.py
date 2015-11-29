from rest_framework import serializers
from names.models import Name


class NameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Name
        fields = ('name', 'used',)

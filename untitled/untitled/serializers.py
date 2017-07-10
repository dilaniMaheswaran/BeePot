from rest_framework import serializers


class TestInit(object):
    def __init__(self,province):
        self.province = province


class TestSerializer(serializers.Serializer):
    province = serializers.CharField(max_length=200)
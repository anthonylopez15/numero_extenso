from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.num_extenso import convert_value
from core.serializers import NumeroSerializer


class NumeroViewSet(ModelViewSet):
    serializer_class = NumeroSerializer

    def retrieve(self, request, *args, **kwargs):

        data = kwargs
        try:
            result = convert_value(data['pk'])
            data = {
                'extenso': result
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e.args[0])
            return Response(status=status.HTTP_400_BAD_REQUEST)

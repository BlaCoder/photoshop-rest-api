from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings

from api.serializer import ImagemSerializer
from api.models import Imagem
from api.utils import Activate

class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer

    def create(self, request, *args, **kwargs):

        informacao = request.data
        msglist = []
        
        try:
            for value in informacao.values():
                msglist.append(value)
            codigo = msglist[2]
            usuario = msglist[1]
            ambiente = msglist[3]
            itens = msglist[4]
            print(Activate.exec(codigo,usuario,ambiente,itens))
        except Exception as e:
            print(e)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
    
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
from django.db.utils import IntegrityError
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError,ParseError
from api.exceptions import Duplicado
from .models import Clientes
from .serializers import ClientesSerializer

class ClientesViewSets(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    authentication_classes = ()
    permission_classes = [AllowAny]

    @action(detail=False, methods=['GET'])
    def get_clientes(self, request, pk=None):
        try:
            clientes = self.get_queryset()
            serializer = self.get_serializer(clientes, many=True)
            return Response({'results':serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error':'este objeto no existe!'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['GET'])
    def get_clientes_by_id(self, request, pk=None):
        try:
            clientes = Clientes.objects.get(id=pk)
            serializer = self.get_serializer(clientes, many=False)
            return Response({'results':serializer.data}, status=status.HTTP_200_OK)
        except ValidationError:
            return Response({'error':'datos incorrectos!'}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({'error':'no existe este cliente!'}, status=status.HTTP_404_NOT_FOUND)
        except MultipleObjectsReturned:
            return Response({'error':'multiples objetos devueltos!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as ex:
            return Response({'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['POST'])
    def create_clientes(self, request, pk=None):
        try:
            data = request.data
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'results':'cliente creado!'}, status=status.HTTP_200_OK)
        except ParseError:
            return Response({'error':'datos incorrectos!'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({'error':'no se pudo validar la data!'}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            raise Duplicado()
        except Exception as ex:
            return Response({'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['DELETE'])
    def delete_clientes(self, request, pk=None):
        try:
            clientes = Clientes.objects.get(id=pk)
            clientes.delete()
            return Response({'results':'cliente eliminado!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error':'este cliente no existe!'}, status=status.HTTP_404_NOT_FOUND)
        except ParseError:
            return Response({'error':'peticion mal estructurada!'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({'error':'fallaron las validaciones!'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['PUT'])
    def update_clientes(self, request, pk=None):
        try:
            clientes = self.get_object()
            serializer = self.get_serializer(clientes, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'results':'cliente actualizado!'}, status=status.HTTP_200_OK)
        except ParseError:
            return Response({'error':'data invalida!'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({'error':'no se pudo validar la data!'}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            raise Duplicado()
        except Exception as ex:
            return Response({'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        



# Create your views here.

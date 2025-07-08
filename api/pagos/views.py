from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError,ValidationError
from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
from django.db.utils import IntegrityError
from .models import Pagos
from .serializers import PagosSerializers
from api.exceptions import Duplicado,ErrorDeParseo,ErrorInterno,ValidacionInvalida,MultiplesResultados,ObjetoNoExiste

class PagosViewSets(viewsets.ModelViewSet):
    queryset = Pagos.objects.all()
    serializer_class = PagosSerializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def get_pagos(self, request, pk=None):
        try:
            pagos = self.get_queryset()
            serialzier = self.get_serializer(pagos, many=True)
            return Response({'results':serialzier.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['GET'])
    def get_pagos_by_id(self, request, pk=None):
        try:
            pagos = Pagos.objects.get(id=pk)
            serializer = self.get_serializer(pagos, many=False)
            return Response({'results':serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except MultipleObjectsReturned:
            raise MultiplesResultados()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=False, methods=['POST'])
    def create_pagos(self, request, pk=None):
        try:
            data = request.data
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'results':'¡creado exitosamente!'}, status=status.HTTP_200_OK)
        except ParseError:
            raise ErrorDeParseo()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno()
        
    @action(detail=True, methods=['DELETE'])
    def delete_pagos(self, request, pk=None):
        try:
            pagos= Pagos.objects.get(id=pk)
            pagos.delete()
            return Response({'results':'¡eliminado exitosamente!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except MultipleObjectsReturned:
            raise MultiplesResultados()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno()
        
    @action(detail=True, methods=['PUT'])
    def update_pagos(self, request, pk=None):
        try:
            pagos = self.get_object()
            serializer = self.get_serializer(pagos, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'results':'¡actualizado exitosamente!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ParseError:
            raise ErrorDeParseo()
        except ValidationError:
            raise ValidacionInvalida()
        except MultipleObjectsReturned:
            raise MultiplesResultados()
        except Exception as ex:
            raise ErrorInterno()

# Create your views here.

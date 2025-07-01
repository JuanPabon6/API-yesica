from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, ValidationError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.utils import IntegrityError
from .models import TiposDeEventos
from .serializers import TiposDeEventosSerializers
from api.exceptions import Duplicado,ErrorInterno,ErrorDeParseo,MultiplesResultados,ValidacionInvalida,ObjetoNoExiste

class TiposDeEventosViewSets(viewsets.ModelViewSet):
    queryset = TiposDeEventos.objects.all()
    serializer_class = TiposDeEventosSerializers
    authentication_classes = ()
    permission_classes = [AllowAny]

    @action(detail=False, methods=['GET'])
    def get_tipos_de_eventos(self, request, pk=None):
        try:
            tipos_eventos = self.get_queryset()
            serializer = self.get_serializer(tipos_eventos, many=True)
            return Response({'results':serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['GET'])
    def get_tipos_de_eventos_by_id(self, request, pk=None):
        try:
            tipos_eventos = TiposDeEventos.objects.get(id=pk)
            serializer = self.get_serializer(tipos_eventos, many=False)
            return Response({'results':serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except MultipleObjectsReturned:
            raise MultiplesResultados()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=False, methods=['POST'])
    def create_tipos_de_eventos(self, request, pk=None):
        try:
            data = request.data
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'results':'creado exitosamente!'}, status=status.HTTP_200_OK)
        except ParseError:
            raise ErrorDeParseo()
        except ValidationError:
            raise ValidacionInvalida()
        except IntegrityError:
            raise Duplicado()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['DELETE'])
    def delete_tipos_de_eventos(self, request, pk=None):
        try:
            tipos_eventos = TiposDeEventos.objects.get(id=pk)
            tipos_eventos.delete()
            return Response({'results':'borrado exitosamente!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['PUT'])
    def update_tipos_de_eventos(self, request, pk=None):
        try:
            tipos_eventos = self.get_object()
            serializer = self.get_serializer(tipos_eventos, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'results':'actualizado con exito!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ParseError:
            raise ErrorDeParseo()
        except ValidationError:
            raise ValidacionInvalida()
        except MultipleObjectsReturned:
            raise MultiplesResultados()
        except IntegrityError:
            raise Duplicado()
        except Exception as ex:
            raise ErrorInterno(str(ex))
            


# Create your views here.

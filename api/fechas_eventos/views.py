from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import status,viewsets
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError, ParseError
from rest_framework.response import Response
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from api.exceptions import ErrorInterno,ErrorDeParseo,MultiplesResultados,ValidacionInvalida,ObjetoNoExiste
from .models import FechasEventos
from .serializers import FechasEventosSerializers

class FechasEventosViewSets(viewsets.ModelViewSet):
    queryset = FechasEventos.objects.all()
    serializer_class = FechasEventosSerializers
    authentication_classes = ()
    permission_classes = [AllowAny]

    @action(detail=False, methods=['GET'])
    def get_fechas_eventos(self, request, pk=None):
        try:
            fechas_eventos = self.get_queryset()
            serializer = self.get_serializer(fechas_eventos, many=True)
            return Response({'results':serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))

    @action(detail=True, methods=['GET'])
    def get_fechas_eventos_by_id(self, request, pk=None):
        try:
            tipos_eventos = FechasEventos.objects.get(id=pk)
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
    def create_fechas_eventos(self, request, pk=None):
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
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['DELETE'])
    def delete_fechas_eventos(self, request, pk=None):
        try:
            tipos_eventos = FechasEventos.objects.get(id=pk)
            tipos_eventos.delete()
            return Response({'results':'borrado exitosamente!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['PUT'])
    def update_fechas_eventos(self, request, pk=None):
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
        except Exception as ex:
            raise ErrorInterno(str(ex))
# Create your views here.

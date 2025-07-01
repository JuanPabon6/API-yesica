from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import status,viewsets
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError, ParseError
from rest_framework.response import Response
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
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
        except ValidationError:
            return Response({'error':'fallaron las validaciones!'}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({'error':'no se encontraron resultados!'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['GET'])
    def get_fechas_eventos_by_id(self, request, pk=None):
        try:
            tipos_eventos = FechasEventos.objects.get(id=pk)
            serializer = self.get_serializer(tipos_eventos, many=False)
            return Response({'results':serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error':'no se encontraron resultados!'}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response({'error':'fallaron las validaciones!'}, status=status.HTTP_400_BAD_REQUEST)
        except MultipleObjectsReturned:
            return Response({'error':'se han devuelto multiples objetos!'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['POST'])
    def create_fechas_eventos(self, request, pk=None):
        try:
            data = request.data
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'results':'creado exitosamente!'}, status=status.HTTP_200_OK)
        except ParseError:
            return Response({'error':'solicitud con data invalida!'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({'error':'fallaron las validaciones'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'error':str(ex)} , status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['DELETE'])
    def delete_fechas_eventos(self, request, pk=None):
        try:
            tipos_eventos = FechasEventos.objects.get(id=pk)
            tipos_eventos.delete()
            return Response({'results':'borrado exitosamente!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error':'no se encontraron resultados!'}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response({'error':'fallaron las validaciones!'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['PUT'])
    def update_fechas_eventos(self, request, pk=None):
        try:
            tipos_eventos = self.get_object()
            serializer = self.get_serializer(tipos_eventos, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'results':'actualizado con exito!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error':'no se encontraron resultados!'}, status=status.HTTP_404_NOT_FOUND)
        except ParseError:
            return Response({'error':'solicitud con data incorrecta!'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({'error':'fallaron las validaciones!'}, status=status.HTTP_400_BAD_REQUEST)
        except MultipleObjectsReturned:
            return Response({'error':'multiples objetos retornados!'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

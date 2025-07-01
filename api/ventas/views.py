from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import status,viewsets
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError, ParseError
from rest_framework.response import Response
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from .models import Ventas
from .serializers import VentasSerializers
from api.exceptions import ErrorDeParseo,ObjetoNoExiste,MultiplesResultados,ValidacionInvalida,ErrorInterno

class VentasViewSets(viewsets.ModelViewSet):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializers
    authentication_classes = ()
    permission_classes = [AllowAny]

    @action(detail=False, methods=['GET'])
    def get_ventas(self, request, pk=None):
        try:
            ventas = self.get_queryset()
            serializer = self.get_serializer(ventas, many=True)
            return Response({'results':serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))

    @action(detail=True, methods=['GET'])
    def get_ventas_by_id(self, request, pk=None):
        try:
            ventas = Ventas.objects.get(id=pk)
            serializer = self.get_serializer(ventas, many=False)
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
    def create_ventas(self, request, pk=None):
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
            import traceback
            print(traceback.format_exc()) 
            raise ErrorInterno({'detail':str(ex)})
        
    @action(detail=True, methods=['DELETE'])
    def delete_ventas(self, request, pk=None):
        try:
            ventas = Ventas.objects.get(id=pk)
            ventas.delete()
            return Response({'results':'¡eliminado exitosamente!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ParseError:
            raise ErrorDeParseo()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['PUT'])
    def update_ventas(self, request, pk=None):
        try:
            ventas = self.get_object()
            serializer = self.get_serializer(ventas, data=request.data)
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
            raise ErrorInterno(str(ex))
    

# Create your views here.

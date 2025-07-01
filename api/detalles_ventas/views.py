from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import status,viewsets
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError, ParseError
from rest_framework.response import Response
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from .models import DetallesVentas
from .serializers import DetallesVentasSerializers
from api.exceptions import ErrorDeParseo,ValidacionInvalida,MultiplesResultados,ObjetoNoExiste,ErrorInterno

class DetallesVentasViewSets(viewsets.ModelViewSet):
    queryset = DetallesVentas.objects.all()
    serializer_class = DetallesVentasSerializers
    authentication_classes = ()
    permission_classes = [AllowAny]

    @action(detail=False, methods=['GET'])
    def get_detalles_de_ventas(self, request, pk=None):
        try:
            detalles_ventas = self.get_queryset()
            serializer = self.get_serializer(detalles_ventas, many=True)
            return Response({'results':serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['GET'])
    def get_detalles_de_ventas_by_id(self, request, pk=None):
        try:
            detalles_ventas = DetallesVentas.objects.get(id=pk)
            serializer = self.get_serializer(detalles_ventas, many=False)
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
    def create_detalles_de_ventas(self, request, pk=None):
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
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['DELETE'])
    def delete_detalles_de_venta(self, request, pk=None):
        try:
            detalles_venta = DetallesVentas.objects.get(id=pk)
            detalles_venta.delete()
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
    def update_detalles_de_venta(self, request, pk=None):
        try:
            detalles_venta = self.get_object()
            serializer = self.get_serializer(detalles_venta, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'results':'¡actualizado exitosamente!'})
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ParseError:
            raise ErrorDeParseo
        except MultipleObjectsReturned:
            raise MultiplesResultados()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))

        

# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import ParseError, ValidationError
from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
from .serializers import FacturasDeClientesSerializers
from .models import FacturasDeClientes
from api.exceptions import ErrorDeParseo,ErrorInterno,ValidacionInvalida,MultiplesResultados,ObjetoNoExiste

class FacturasDeClientesViewSets(viewsets.ModelViewSet):
    queryset = FacturasDeClientes.objects.all()
    serializer_class = FacturasDeClientesSerializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def get_facturas_de_clientes(self, request, pk=None):
        try:
            facturas = self.get_queryset()
            serializer = self.get_serializer(facturas, many=True)
            return Response({'results':serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['GET'])
    def get_facturas_de_clientes_by_id(self, request, pk=None):
        try:
            facturas = FacturasDeClientes.objects.get(id=pk)
            serializer = self.get_serializer(facturas, pk=False)
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
    def create_facturas_de_clientes(self, request, pk=None):
        try:
            data=request.data
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
    def delete_facturas_de_clientes(self, request, pk=None):
        try:
            facturas = FacturasDeClientes.objects.get(id=pk)
            facturas.delete()
            return Response({'results':'¡eliminado exitosamente!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except MultipleObjectsReturned:
            raise MultiplesResultados()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['PUT'])
    def update_facturas_de_clientes(self, request, pk=None):
        try:
            facturas = self.get_object()
            serializer = self.get_serializer(facturas, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'results':'¡actualizado exitosamente!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ParseError:
            raise ErrorDeParseo()
        except MultipleObjectsReturned:
            raise MultiplesResultados()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=False, methods=['GET'])
    def get_facturas_de_clientes_by_fecha(self, request, pk=None):
        try:
            documento = request.query_params.get('Identificacion')
            fecha = request.query_params.get('fecha_evento')
            if not documento or not fecha:
                return Response({'error':'¡hacen falta parametros!', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
            
            factura = FacturasDeClientes.objects.filter(Identificacion=documento, fecha_evento=fecha)
            if factura.exists():
                serializer = self.get_serializer(factura, many=False)
                return Response({'results':serializer.data, 'success':True}, status=status.HTTP_200_OK)
            else:
                return Response({'results':None, 'success':False}, status=status.HTTP_404_NOT_FOUND)
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
        
    @action(detail=False, methods=['GET'])
    def get_all_facturas_de_clientes(self, request, pk=None):
        try:
            documento = request.query_params.get('Identificacion')
            if not documento:
                return Response({'error':'¡hacen falta parametros!', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
            
            facturas = FacturasDeClientes.objects.filter(Identificacion=documento)
            if facturas.exists():
                serializer = self.get_serializer(facturas, many=True)
                return Response({'results':serializer.data,  'success':True}, status=status.HTTP_200_OK)
            else:
                return Response({'results':[], 'success':False}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ParseError:
            raise ErrorDeParseo()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))

# Create your views here.


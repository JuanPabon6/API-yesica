from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ParseError,ValidationError
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
from .models import DetallesPagos
from .serializers import DetallesPagosSerializers
from api.exceptions import ErrorDeParseo,ErrorInterno,MultiplesResultados,ValidacionInvalida,ObjetoNoExiste

class DetallePagosViewSets(viewsets.ModelViewSet):
    queryset = DetallesPagos.objects.all()
    serializer_class = DetallesPagosSerializers
    authentication_classes = ()
    permission_classes = [AllowAny]

    @action(detail=False, methods=['GET'])
    def get_detalles_pagos(self, request, pk=None):
        try:
            pagos = self.get_queryset()
            serializer = self.get_serializer(pagos, many=True)
            return Response({'results':serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['GET'])
    def get_detalles_pagos_by_id(self, request, pk=None):
        try:
            pagos = DetallesPagos.objects.get(id=pk)
            serializer = self.get_serializer(pagos, many=False)
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
    def create_detalles_pagos(self, request, pk=None):
        try:
            data = request.data
            serialzier = self.get_serializer(data=data)
            serialzier.is_valid(raise_exception=True)
            serialzier.save()
            return Response({'results':'¡creado exitosamente'}, status=status.HTTP_200_OK)
        except ParseError:
            raise ErrorDeParseo()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['DELETE'])
    def delete_detalles_pagos(self, request, pk=None):
        try:
            pagos = DetallesPagos.objects.get(id=pk)
            pagos.delete()
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
    def update_detalles_pagos(self, request, pk=None):
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
            raise ErrorInterno(str(ex))
        
    @action(detail=False, methods=['GET'])
    def get_detalles_pagos_by_nombre(self, request, pk=None):
        try:
            nombre = request.query_params.get('Nombres')
            if not nombre:
                return Response({'error':"¡hacen falta parametros!", 'success':False}, status=status.HTTP_400_BAD_REQUEST)
            
            pago = DetallesPagos.objects.filter(Nombres=nombre)
            if pago.exists():
                serializer = self.get_serializer(pago, many=False)
                return Response({'results':serializer.data, 'success':True}, status=status.HTTP_200_OK)
            else:
                return Response({'results': None, 'success':False}, status=status.HTTP_400_BAD_REQUEST)
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
    def get_all_detalles_pagos_by_nombre(self, request, pk=None):
        try:
            nombre = request.query_params.get('Nombres')
            if not nombre:
                return Response({'error':'¡hacen falta parametros!', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
            
            pagos = DetallesPagos.objects.filter(Nombre=nombre)
            if pagos.exists():
                serializer = self.get_serializer(pagos, many=True)
                return Response({'results':serializer.data, 'success':True}, status=status.HTTP_200_OK)
            else:
                return Response({'error':[], 'success':False}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ParseError:
            raise ErrorDeParseo()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))



# Create your views here.

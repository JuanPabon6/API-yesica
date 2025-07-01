from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ParseError,ValidationError
from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
from django.db.utils import IntegrityError
from .models import FormasPagos
from .serializers import FormasPagosSerializers
from api.exceptions import ErrorDeParseo,ErrorInterno,MultiplesResultados,Duplicado,ValidacionInvalida,ObjetoNoExiste

class FormasPagosViewSets(viewsets.ModelViewSet):
    queryset = FormasPagos.objects.all()
    serializer_class = FormasPagosSerializers
    authentication_classes = ()
    permission_classes = [AllowAny]

    @action(detail=False, methods=['GET'])
    def get_formas_de_pagos(self, request, pk=None):
        try:
            formas_pagos = self.get_queryset()
            serializer = self.get_serializer(formas_pagos, many=True)
            return Response({'results':serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))

    @action(detail=True, methods=['GET'])
    def get_formas_de_pagos_by_id(self, request, pk=None):
        try:
            formas_pagos = FormasPagos.objects.get(id=pk)
            serializer = self.get_serializer(formas_pagos, many=False)
            return Response({'results':serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=False, methods=['POST'])
    def create_formas_de_pago(self, request, pk=None):
        try:
            data = request.data
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'results':'¡creado exitosamente!'}, status=status.HTTP_200_OK)
        except ParseError:
            raise ErrorDeParseo()
        except IntegrityError:
            raise Duplicado()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['DELETE'])
    def delete_formas_de_pago(self, request, pk=None):
        try:
            formas_pago = FormasPagos.objects.get(id=pk)
            formas_pago.delete()
            return Response({'results':'¡eliminado exitosamente!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['PUT'])
    def update_formas_de_pagos(self, request, pk=None):
        try:
            formas_pago =  self.get_object()
            serializer = self.get-serializer(formas_pago, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'results':'¡actualizado correctamente!'})
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
# Create your views here.

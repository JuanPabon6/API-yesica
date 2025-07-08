from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import ParseError,ValidationError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import Compras
from .serializers import ComprasSerializers
from api.exceptions import ObjetoNoExiste, ErrorDeParseo,ErrorInterno,MultiplesResultados,ValidacionInvalida

class ComprasViewSets(viewsets.ModelViewSet):
    queryset = Compras.objects.all()
    serializer_class = ComprasSerializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def get_compras(self, request, pk=None):
        try:
            compras = self.get_queryset()
            serializer = self.get_serializer(compras, many=True)
            return Response({'results':serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['GET'])
    def get_compras_by_id(self, request, pk=None):
        try:
            compras = Compras.objects.get(id=pk)
            serializer = self.get_serializer(compras, many=False)
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
    def create_compras(self, request, pk=None):
        try:
            data = request.data
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'reuslts':'¡creado exitosamente!'}, status=status.HTTP_200_OK)
        except ParseError:
            raise ErrorDeParseo()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['DELETE'])
    def delete_compras(self, request, pk=None):
        try:
            compra = Compras.objects.get(id=pk)
            compra.delete()
            return Response({'results':'¡eliminado exitosamente!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except ParseError:
            raise ErrorDeParseo()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['PUT'])
    def update_compras(self, request, pk=None):
        try:
            compras = self.get_object()
            serializer = self.get_serializer(compras, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'results':'¡actualizado exitosamente!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ParseError:
            raise ErrorDeParseo()
        except ValidationError:
            raise ValidationError()
        except MultipleObjectsReturned:
            raise MultiplesResultados()
        except Exception as ex:
            raise ErrorInterno(str(ex))

# Create your views here.

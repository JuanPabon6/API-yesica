from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ParseError,ValidationError
from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
# from django.db.utils import IntegrityError
from .models import Materiales
from .serializers import MaterialesSerializers
from api.exceptions import ErrorDeParseo,ErrorInterno,MultiplesResultados,Duplicado,ValidacionInvalida,ObjetoNoExiste

class MaterialesViewSets(viewsets.ModelViewSet):
    queryset = Materiales.objects.all()
    serializer_class = MaterialesSerializers
    authentication_classes = ()
    permission_classes = [AllowAny]

    @action(detail=False, methods=['GET'])
    def get_materiales(self, request, pk=None):
        try:
            materiales = self.get_queryset()
            serializer = self.get_serializer(materiales, many=True)
            return Response({'results':serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))

    @action(detail=True, methods=['GET'])
    def get_materiales_by_id(self, request, pk=None):
        try:
            materiales = Materiales.objects.get(id=pk)
            serializer = self.get_serializer(materiales, many=False)
            return Response({'resutls':serializer.data}, status=status.HTTP_200_OK) 
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=False, methods=['POST'])
    def create_materiales(self, request, pk=None):
        try:
            data= request.data
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'results':'¡creado exitosamente!'}, status=status.HTTP_200_OK)
        except ParseError:
            ErrorDeParseo()
        except ValidationError:
            raise ValidacionInvalida()
        except MultipleObjectsReturned:
            raise MultiplesResultados()
        except Exception as ex:
            raise ErrorInterno(str(ex))

    @action(detail=True, methods=['DELETE'])
    def delete_materiales(self, request, pk=None):
        try:
            materiales = Materiales.objects.get(id=pk)
            materiales.delete()
            return Response({'results':'eliminado exitosamente'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ParseError:
            raise ErrorDeParseo()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['PUT'])
    def update_materiales(self, request, pk=None):
        try:
            materiales = self.get_object()
            serializer = self.get_serializer(materiales, data=request.data)
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
# Create your views here.

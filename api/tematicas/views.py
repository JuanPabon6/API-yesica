from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError, ParseError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned 
from django.db.utils import IntegrityError
from .models import Tematicas
from .serializers import TematicasSerializer
from api.exceptions import Duplicado,ErrorDeParseo,ErrorInterno,MultiplesResultados,ValidacionInvalida,ObjetoNoExiste

class TematicasViewSets(viewsets.ModelViewSet):
    queryset = Tematicas.objects.all()
    serializer_class = TematicasSerializer
    authentication_classes = ()
    permission_classes = [AllowAny]

    @action(detail=False, methods=['GET'])
    def get_tematicas(self, request, pk=None):
        try:
            tematicas = self.get_queryset()
            serializer = self.get_serializer(tematicas, many=True)
            return Response({'results':serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['GET'])
    def get_tematicas_by_id(self, request, pk=None):
        try:
            tematicas = Tematicas.objects.get(id=pk)
            serializer = self.get_serializer(tematicas, many=False)
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
    def create_tematicas(self, request, pk=None):
        try:
            data = request.data
            serializer  = self.get_serializer(data=data)
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
    def delete_tematicas(self, request, pk=None):
        try:
            tematicas = Tematicas.objects.get(id=pk)
            tematicas.delete()
            return Response({'results':'eliminado exitosamente!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))
        
    @action(detail=True, methods=['PUT'])
    def update_tematicas(self, request, pk=None):
        try:
            tematicas = self.get_object()
            serializer = self.get_serializer(tematicas, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'results':'actualizado correctamente!'}, status=status.HTTP_200_OK)
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

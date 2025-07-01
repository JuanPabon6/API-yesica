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
from api.exceptions import Duplicado

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
            return Response({'error':'no se encontraron resultados!'}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response({'error':'fallaron las validaciones!'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['GET'])
    def get_tematicas_by_id(self, request, pk=None):
        try:
            tematicas = Tematicas.objects.get(id=pk)
            serializer = self.get_serializer(tematicas, many=False)
            return Response({'results':serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error':'no se encontraron resultados!'}, status=status.HTTP_404_NOT_FOUND)
        except MultipleObjectsReturned:
            return Response({'error':'multiples objetos retornados!'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({'error':'fallaron las validaciones!'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['POST'])
    def create_tematicas(self, request, pk=None):
        try:
            data = request.data
            serializer  = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'results':'creado exitosamente!'}, status=status.HTTP_200_OK)
        except ParseError:
            return Response({'error':'solicitud mal estructurada!'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({'error':'fallaron las validaciones!'}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            raise Duplicado()
        except Exception as ex:
            return Response({'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['DELETE'])
    def delete_tematicas(self, request, pk=None):
        try:
            tematicas = Tematicas.objects.get(id=pk)
            tematicas.delete()
            return Response({'results':'eliminado exitosamente!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error':'no se encontraron resultados!'}, status=status.HTTP_404_NOT_FOUND)
        except ParseError:
            return Response({'error':'peticion mal estructurada!'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({'error':'fallaron las validaciones!'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['PUT'])
    def update_tematicas(self, request, pk=None):
        try:
            tematicas = self.get_object()
            serializer = self.get_serializer(tematicas, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'results':'actualizado correctamente!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error':'no se encontraron resultados!'}, status=status.HTTP_404_NOT_FOUND)
        except ParseError:
            return Response({'error':'la solicitud es incorrecta!'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({'error':'fallaron las validaciones!'}, status=status.HTTP_400_BAD_REQUEST)
        except MultipleObjectsReturned:
            return Response({'error':'multiples objetos devueltos!'}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            raise Duplicado()
        except Exception as ex:
            return Response({'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.

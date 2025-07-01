from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import status,viewsets
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError, ParseError
from rest_framework.response import Response
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db.utils import IntegrityError
from api.exceptions import Duplicado, ErrorInterno, ObjetoNoExiste, ErrorDeParseo, ValidacionInvalida
from .models import Empleados 
from .serializers import EmpleadosSerializers

class EmpleadosViewSets(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializers
    authentication_classes = ()
    permission_classes = [AllowAny]

    @action(detail=False, methods=['GET'])
    def get_empleados(self, request, pk=None):
        try:
            empleados = self.get_queryset()
            serializer = self.get_serializer(empleados, many=True)
            return Response({'results':serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error':'no se encontraron resultados!'}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response({'error':'fallaron las validaciones!'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['GET'])
    def get_empleados_by_id(self, request, pk=None):
        try:
            empleados = Empleados.objects.get(id=pk)
            serializer = self.get_serializer(empleados, many=False)
            return Response({'results':serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error':'no se encontraron resultados!'}, status=status.HTTP_404_NOT_FOUND)
        except MultipleObjectsReturned:
            return Response({'error':'multiples objetos devueltos!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as ex:
            return Response({'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['POST'])
    def create_empleados(self, request, pk=None):
        try:
            data = request.data
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'results':'empleado creado!'}, status=status.HTTP_200_OK)
        except ParseError:
            return Response({'error':'solicitud mal estructurada!'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({'error':'fallaron las validaciones!'}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            raise Duplicado()
        except Exception as ex:
            return Response({'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['DELETE'])
    def delete_empleados(self, request, pk=None):
        try:
            empleados = Empleados.objects.get(id=pk)
            empleados.delete()
            return Response({'results':'empleado eliminado!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error':'el empleado no existe!'}, status=status.HTTP_404_NOT_FOUND)
        except ParseError:
            return Response({'error':'solicitud mal formada!'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({'error':'fallaron las validaciones!'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['PUT'])
    def update_empleados(self, request, pk=None):
        try:
            empleados = self.get_object()
            serializer = self.get_serializer(empleados, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'results':'empleado actualizado!'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error':'empleado no encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        except ParseError:
            return Response({'error':'solicitud mal formada!'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({'error':'fallaron las validaciones!'}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            raise Duplicado()
        except Exception as ex:
            raise ErrorInterno(str(ex))

    @action(detail=False, methods=['GET'])
    def login(self, request, pok=None):
        try:
            data = request.data
            login = Empleados.objects.filter(Email=data["Email"], contraseña=data["contraseña"])

            if login.exists():
                serializer = self.get_serializer(login.first(), many=False)
                return Response({'results':serializer.data, "succes":True}, status=status.HTTP_200_OK)
            else:
                return Response({'results':{}, "success":False}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise ObjetoNoExiste()
        except ParseError:
            raise ErrorDeParseo()
        except ValidationError:
            raise ValidacionInvalida()
        except Exception as ex:
            raise ErrorInterno(str(ex))


# Create your views here.

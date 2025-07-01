from rest_framework.exceptions import APIException

#ObjectDoesNotExist
class ObjetoNoExiste(APIException):
    status_code = 404
    default_detail = "!este objeto no existe!"
    default_code = "objeto_no_encontrado"

#ValidationError
class ValidacionInvalida(APIException):
    status_code = 400
    default_detail = "!los datos enviados no son corectos!"
    default_code = "validacion_incorrecta"

#ParseError
class ErrorDeParseo(APIException):
    status_code = 400
    default_detail = "¡no se pudieron interpretar los datos enviados!"
    default_code = "error_de_parseo"

#MultipleObjectReturned
class MultiplesResultados(APIException):
    status_code = 400
    default_detail = "¡se encontraron multiples resultados! , solo se espera uno!"
    default_code = "multiples_objetos"

#PermissionDenied
class ObjetoDuplicado(APIException):
    status_code = 409
    default_detail = "¡Este objeto ya existe!"
    default_code = "objeto_duplicado"

#PermissionDenied
class SinPermisos(APIException):
    status_code = 403
    default_detail = "¡No tienes permisos para ingresar aqui!"
    default_code = "sin_permisos"

#SuspiciousOperation
class AlertaDeSeguridad(APIException):
    status_code = 400
    default_detail = "¡Se encontro algo sospechoso en tu peticion!"
    default_code = "peticion_sospechosa"

#Exception
class ErrorInterno(APIException):
    status_code = 500
    default_detail = "¡Ha ocurrido un error en el servidor!"
    default_code = "error_de_servidor"
    def __init__(self, detail=None):
        if detail is None:
            detail = self.default_detail
        super().__init__(detail)

#IntegrityError o ValidationError
class Duplicado(APIException):
    status_code = 409
    default_detail = "¡Este objeto ya existe!"
    default_code = "objeto_duplicado"
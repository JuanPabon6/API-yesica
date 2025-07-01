from django.urls import path, include

urlpatterns = [
    path('clientes/', include('api.clientes.urls')),
    path('empleados/', include('api.empleados.urls')),
    path('tipos_eventos/', include('api.tipos_eventos.urls')),
    path('tematicas/', include('api.tematicas.urls')),
    path('fechas_eventos/', include('api.fechas_eventos.urls')),
    path('ventas/', include('api.ventas.urls')),
    path('detalles_ventas/', include('api.detalles_ventas.urls')),
    path("detalles_pagos/", include('api.detalles_pagos.urls')),
    path('pagos/', include('api.pagos.urls')),
    path('formas_pagos/', include('api.formas_pago.urls')),
    path('materiales/', include('api.materiales.urls')),
    path('compras/', include('api.compras.urls')),
    path('facturas_de_clientes/', include('api.facturas_clientes.urls'))
]

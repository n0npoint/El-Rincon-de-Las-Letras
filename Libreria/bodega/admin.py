from django.contrib import admin



from .administrador.adminLibroxProveedor import AdminTbLibroxProveedor

from .administrador.adminLibroxPedido import AdminTbLibroxPedido

from .administrador.adminEditorialxproveedor import AdminEditorialxProveedor

from .administrador.adminPedido import AdminPedido

from .administrador.AdminProveedor import AdminTbProveedor

from .administrador.adminEditorial import AdminEditorial

from .administrador.tablasCurzadas import AdminCategoriaxLibros

from .administrador.adminCategoria import AdminCategoria



#importacion de los modelos
from .models.autor import *
from .models.categoria import *
from .models.editorial import TbEditorial
from .models.inventario import TbInventario                                      
from .models.libro import *
from .models.proveedor import *
from .models.pedido import *
from .models.categoriaXlibro import *
from .models.editoriaXproveedor import *
from .models.libroXpedido import *
from .models.librXproveedor import *


from .administrador.adminAutor import AdminAutor
from .administrador.adminLibros import AdminLibro

#Se agregan los modelos al panel de Administracion
admin.site.register(TbAutor , AdminAutor)
admin.site.register(TbCategoria , AdminCategoria)
admin.site.register(TbEditorial , AdminEditorial)
admin.site.register(TbLibros , AdminLibro)
admin.site.register(TbProveedor , AdminTbProveedor)
admin.site.register(TbPedidos , AdminPedido)
admin.site.register(TbCategoriaxlibro , AdminCategoriaxLibros)
admin.site.register(TbEditorialxproveedor , AdminEditorialxProveedor)
admin.site.register(TbLibroxpedido , AdminTbLibroxPedido)
admin.site.register(TbLibroxproveedor , AdminTbLibroxProveedor)




admin.site.register(TbInventario)
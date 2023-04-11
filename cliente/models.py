from django.db import models

# Create your models here.
# ------------------------------------------APARTADO DE CLIENTE--------------------------------------

# ------------------------------------------Equipos--------------------------------------------------

class Equipos(models.Model):
    nombre_equi = models.CharField(primary_key=True, max_length=20, null=False)

    def __str__(self):
        return self.nombre_equi

    class Meta:
        db_table = 'Equipo'
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['nombre_equi']
# ---------------------------------------------------------------------------------------------------


# ------------------------------------------Municipio------------------------------------------------
class Municipio(models.Model):
    nombreMunicipio = models.CharField(primary_key=True, max_length=30, null=False)

    def __str__(self):
        return self.nombreMunicipio

    class Meta:
        db_table = 'Municipio'
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        ordering = ['nombreMunicipio']
# ---------------------------------------------------------------------------------------------------


# ------------------------------------------Tipo_Instalacion-----------------------------------------
class Tipo_Instalacion(models.Model):
    tipo_ins = models.CharField(primary_key=True, max_length=20, null=False)

    def __str__(self):
        return self.tipo_ins

    class Meta:
        db_table = 'Tipo_Instalacion'
        verbose_name = 'Tipo_Instalacion'
        verbose_name_plural = 'Tipos_Instalaciones'
        ordering = ['tipo_ins']
# ---------------------------------------------------------------------------------------------------


# ------------------------------------------Tecnico-----------------------------------------
class Tecnico(models.Model):
    nombre_tecnico = models.CharField(primary_key=True, max_length=40, null=False)

    def __str__(self):
        return self.nombre_tecnico

    class Meta:
        db_table = 'Nombre del tecnico'
        verbose_name = 'Nombre Tecnico'
        verbose_name_plural = 'Nombres del Tecnico'
        ordering = ['nombre_tecnico']
# ---------------------------------------------------------------------------------------------------


# ------------------------------------------Ap del cliente-----------------------------------------
class Ap(models.Model):
    nombreAp = models.CharField(primary_key=True, max_length=30,blank=True,null=False)

    def __str__(self):
        return self.nombreAp

    class Meta:
        db_table = 'Ap'
        verbose_name = 'Ap'
        verbose_name_plural = 'Ap'
        ordering = ['nombreAp']
# ---------------------------------------------------------------------------------------------------


# ------------------------------------------Cliente--------------------------------------------------
class Cliente(models.Model):
    ESTADO_CHOICES = (
        ('Activos', 'Activos'),
        ('Suspendidos', 'Suspendidos'),
        ('REquipos', 'REquipos'),
        ('Retiros', 'Retiros'),
    )
    ip = models.CharField(max_length=13, null=True, blank=True, unique=True)
    cedula = models.CharField(max_length=20, null=False)
    nombre = models.CharField(max_length=80, null=False)
    telefono_uno = models.CharField(max_length=13, null=True, blank=True)
    telefonos_dos = models.CharField(max_length=13, null=True, blank=True)
    valor_instalacion = models.CharField(max_length=10, null=True, blank=True)
    fecha_instalacion = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=25, null=True, blank=True)
    estado = models.CharField(max_length=13, choices=ESTADO_CHOICES, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, null=True, blank=True)
    equipos = models.ForeignKey(Equipos, on_delete=models.SET_NULL, null=True, blank=True)
    tipo_instalacion = models.ForeignKey(Tipo_Instalacion, on_delete=models.SET_NULL, null=True, blank=True)
    cap_megas = models.CharField(max_length=25, null=True, blank=True)
    ap = models.ForeignKey(Ap,on_delete=models.SET_NULL,null=True, blank=True)
    nombre_tecnico = models.ForeignKey(Tecnico,on_delete=models.SET_NULL,null=True, blank=True)

    class Meta:
        db_table = 'Cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['ip']

    def __str__(self):
        return self.nombre 

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.strip()
        super().save(*args, **kwargs)

    @classmethod
    def numeroRegistrados(self):
        return int(self.objects.all().count())

    @classmethod
    def ipRegistradas(self):
        objetos = self.objects.all().order_by('ip')
        arreglo = []
        for indice, objeto in enumerate(objetos):
            arreglo.append([])
            arreglo[indice].append(objeto.ip)
            nombre_cliente = objeto.nombre
            arreglo[indice].append("%s. I.P: %s" % (
                nombre_cliente, self.formatearIp(objeto.ip)))
        return arreglo

    @staticmethod
    def formatearIp(ip):
        return str.format((ip), '.d')
    
# ---------------------------------------------------------------------------------------------------


# ------------------------------------------Cliente Retirado-----------------------------------------
class ClienteRetirado(models.Model):
    ESTADO_CHOICES = (
        ('Activos', 'Activos'),
        ('Suspendidos', 'Suspendidos'),
        ('REquipos', 'REquipos'),
        ('Retiros', 'Retiros'),
    )
    ip = models.CharField(max_length=13, null=True, blank=True, unique=True)
    cedula = models.CharField(max_length=10, null=False, unique=True)
    nombre = models.CharField(max_length=80, null=False)
    telefono_uno = models.CharField(max_length=13, null=True, blank=True)
    telefonos_dos = models.CharField(max_length=13, null=True, blank=True)
    valor_instalacion = models.CharField(max_length=10, null=True, blank=True)
    fecha_instalacion = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=25, null=True, blank=True)
    estado = models.CharField(max_length=13, choices=ESTADO_CHOICES, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, null=True, blank=True)
    equipos = models.ForeignKey(Equipos, on_delete=models.SET_NULL, null=True, blank=True)
    tipo_instalacion = models.ForeignKey(Tipo_Instalacion, on_delete=models.SET_NULL, null=True, blank=True)
    cap_megas = models.CharField(max_length=25, null=True, blank=True)
    ap = models.ForeignKey(Ap,on_delete=models.SET_NULL,null=True, blank=True)
    nombre_tecnico = models.ForeignKey(Tecnico,on_delete=models.SET_NULL,null=True, blank=True)
    fecha_retirado = models.DateField(auto_now_add=True, blank=True, null=True)

    class Meta:
        db_table = 'Cliente_Retirado'
        verbose_name = 'Cliente_Retirado'
        verbose_name_plural = 'Clientes_Retirados'

    @classmethod
    def numeroRetirados(self):
        return int(self.objects.all().count())



# ---------------------------------------------------------------------------------------------------
# -------------------------------------FIN DEL APARTADO CLIENTE--------------------------------------


# -------------------------------------APARTADO DE FACTURA-------------------------------------------
# ------------------------------------------Detalle--------------------------------------------------
class Detalle(models.Model):
    detalle = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.detalle

    class Meta:
        db_table = 'Detalle'
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalles'
        ordering = ['id']

    def save(self, *args, **kwargs):
        self.detalle = self.detalle.strip()
        super().save(*args, **kwargs)

# ---------------------------------------------------------------------------------------------------


# -------------------------------------FACTURA-------------------------------------------------------
class Factura(models.Model):
    TIPO_CHOICES = (
        ('#Recibo', '#Recibo'),
        ('Bancos', 'Bancos'),
        ('Acertemos', 'Acertemos'),
        ('Nequi', 'Nequi'),
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    detalle = models.ForeignKey(Detalle, on_delete=models.SET_NULL, null=True)
    tipo_pago = models.CharField(max_length=15, choices=TIPO_CHOICES, null=True,blank=True)
    valor_pago = models.CharField(max_length=15, null=True, blank=True)
    n_recibo = models.CharField(max_length=6, null=True, blank=True)
    fecha_pago = models.DateField(null=True, blank=True, verbose_name='Fecha de pago (Opcional)')
    fecha_vencimiento = models.DateField(null=True, blank=True, verbose_name='Fecha de vencimiento (Opcional)')
    
    
    @classmethod
    def facturasRegistradas(self):
        return int(self.objects.all().count() )   

# ---------------------------------------------------------------------------------------------------


# -------------------------------------FACTURA RETIRADA-------------------------------------------------------
class FacturaRetirada(models.Model):
    TIPO_CHOICES = (
        ('Mensualidad', 'Mensualidad'),
        ('Banco', 'Banco'),
        ('Acertemos', 'Acertemos'),
    )
    cliente_retirado = models.ForeignKey(ClienteRetirado, on_delete=models.SET_NULL,blank=True, null=True)
    detalle = models.ForeignKey(Detalle, on_delete=models.SET_NULL, null=True)
    tipo_pago = models.CharField(max_length=15, choices=TIPO_CHOICES, null=True,blank=True)
    valor_pago = models.CharField(max_length=15, null=True, blank=True)
    fecha_pago = models.DateField(null=True, blank=True, verbose_name='Fecha de pago (Opcional)')
    fecha_vencimiento = models.DateField(null=True, blank=True, verbose_name='Fecha de vencimiento (Opcional)')
    
# ---------------------------------------------------------------------------------------------------
# -------------------------------------FIN DEL APARTADO FACTURA--------------------------------------

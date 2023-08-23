import os
import miniupnpc

# Función para abrir el puerto UPnP
def abrir_puerto_UPnP(port, protocol, description):
    u = miniupnpc.UPnP()
    u.discoverdelay = 200
    u.discover()
    u.selectigd()
    u.addportmapping(port, protocol, u.lanaddr, port, description, '')

# Define las carpetas que deseas sincronizar
carpeta_origen = "/ruta/de/origen"
carpeta_destino = "/ruta/de/destino"

# Abre el puerto UPnP
puerto = 2234
protocolo = "TCP"
descripcion_puerto = "Sincronización de carpetas"

abrir_puerto_UPnP(puerto, protocolo, descripcion_puerto)

# Realiza la sincronización de carpetas
print(f"Sincronizando la carpeta '{carpeta_origen}' con la carpeta '{carpeta_destino}'")

# Copia los archivos de la carpeta origen a la carpeta destino
for archivo in os.listdir(carpeta_origen):
    origen = os.path.join(carpeta_origen, archivo)
    destino = os.path.join(carpeta_destino, archivo)
    if os.path.isfile(origen):
        try:
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            shutil.copy2(origen, destino)
            print(f"Copiado: {origen} -> {destino}")
        except Exception as e:
            print(f"Error al copiar '{origen}': {str(e)}")

print("Sincronización completada")

# Cierra el puerto UPnP (opcional)
# u.deleteportmapping(puerto, protocolo)

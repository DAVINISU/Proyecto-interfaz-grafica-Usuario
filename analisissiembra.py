from statistics import median
import pandas as pd

# leer base de datos de siembras
tablasiembras = pd.read_csv('./Siembras.csv')

# filtro 1 Datos por municipio:
Datospormunicipio = tablasiembras[(tablasiembras["Ciudad"] == "Andes") | (tablasiembras["Ciudad"] == "Barbosa") | (
    tablasiembras["Ciudad"] == "Caldas") | (tablasiembras["Ciudad"] == "Támesis") | (tablasiembras["Ciudad"] == "Yarumal")]

# Exportar tabla
archivoHTML = Datospormunicipio.to_html()
# abrir archivo
ArchivoTEXTO = open("Datospormunicipio.html", "w", encoding="UTF-8")
# escribir en el archivo
ArchivoTEXTO.write(archivoHTML)
# cerrar archivo
ArchivoTEXTO.close()


# filtro 2 Los datos de MEDELLIN ordenados de mayor a menor número de arboles
DatosMedellin1 = tablasiembras[(tablasiembras["Ciudad"] == "Medellín")]
DatosMedellin = DatosMedellin1.sort_values('Arboles', ascending=False)
# Exportar tabla
archivoHTML = DatosMedellin.to_html()
# abrir archivo
ArchivoTEXTO = open("DatosMedellin.html", "w", encoding="UTF-8")
# escribir en el archivo
ArchivoTEXTO.write(archivoHTML)
# cerrar archivo
ArchivoTEXTO.close()

# filtro 3 Los datos de CAUCASIA incluyendo el número de hectáreas sembradas
DatosCaucasia1 = tablasiembras[(tablasiembras["Ciudad"] == "Caucasia")]
DatosCaucasia = DatosCaucasia1[['Hectareas']]
# Exportar tabla
archivoHTML = DatosCaucasia.to_html()
# abrir archivo
ArchivoTEXTO = open("DatosCaucasia.html", "w", encoding="UTF-8")
# escribir en el archivo
ArchivoTEXTO.write(archivoHTML)
# cerrar archivo
ArchivoTEXTO.close()

# filtro 4 Los datos de CAUCASIA incluyendo el número de hectáreas sembradas
DatosSantaFedeAntioquia = tablasiembras[(
    tablasiembras["Ciudad"] == "Santa Fe de Antioquia") & (tablasiembras["Arboles"] > 250)]
DatosSantaFedeAntioquia = DatosSantaFedeAntioquia.sort_values(
    'Arboles', ascending=False)

# Exportar tabla
archivoHTML = DatosSantaFedeAntioquia.to_html()
# abrir archivo
ArchivoTEXTO = open("DatosSantaFedeAntioquia.html", "w", encoding="UTF-8")
# escribir en el archivo
ArchivoTEXTO.write(archivoHTML)
# cerrar archivo
ArchivoTEXTO.close()

# filtro 5 Los datos de las veredas Rio Arriba y la Salazar de Belmira
DatosrioArribayBelmira = tablasiembras[(
    tablasiembras["Vereda"] == "Rio Arriba") | (tablasiembras["Vereda"] == "La Salazar")]
# Exportar tabla
archivoHTML = DatosrioArribayBelmira.to_html()
# abrir archivo
ArchivoTEXTO = open("DatosrioArribayBelmira.html", "w", encoding="UTF-8")
# escribir en el archivo
ArchivoTEXTO.write(archivoHTML)
# cerrar archivo
ArchivoTEXTO.close()

# filtro 6 Los datos de la veredas Quitasol de BELLO ordenados de menor a mayor y el promedio de arboles sembrados en esta vereda
DatosQuitasol = tablasiembras[(
    tablasiembras["Ciudad"] == "Bello") & (tablasiembras["Vereda"] == "Quitasol")]
DatosQuitasol = DatosQuitasol.sort_values('Arboles', ascending=True)
DatosQuitasol = DatosQuitasol.assign(Promedio=DatosQuitasol['Arboles'].mean())
# Exportar tabla
archivoHTML = DatosQuitasol.to_html()
# abrir archivo
ArchivoTEXTO = open("DatosQuitasol.html", "w", encoding="UTF-8")
# escribir en el archivo
ArchivoTEXTO.write(archivoHTML)
# cerrar archivo
ArchivoTEXTO.close()


# filtro 7 Los datos de la veredas Quitasol de BELLO ordenados de menor a mayor y el promedio de arboles sembrados en esta vereda
Datoscaramanta = tablasiembras[(
    tablasiembras["Ciudad"] == "Caramanta")]
print(Datoscaramanta)
# Exportar tabla
archivoHTML = Datoscaramanta.to_html()
# abrir archivo
ArchivoTEXTO = open("Datoscaramanta.html", "w", encoding="UTF-8")
# escribir en el archivo
ArchivoTEXTO.write(archivoHTML)
# cerrar archivo
ArchivoTEXTO.close()

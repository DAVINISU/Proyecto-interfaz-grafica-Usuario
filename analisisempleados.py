
import pandas as pd

# leer base de datos
tablaEmpleados = pd.read_csv('./empleados.csv')
#imprimir tablas
#print(tablaEmpleados.to_string())

# filtro 1 quiero obtener todos los datos de los analistas 1
tablaAnalistas1 = tablaEmpleados[tablaEmpleados["cargo"]=="analista1"].head(50)

# Exportar tabla
archivoHTML = tablaAnalistas1.to_html()
#abrir archivo
ArchivoTEXTO = open("datosanalista1.html","w",encoding="UTF-8")
#escribir en el archivo
ArchivoTEXTO.write(archivoHTML)
#cerrar archivo
ArchivoTEXTO.close()


# filtro 2 quiero obtener todos los datos de los analistas 2
tablaAnalistas2 = tablaEmpleados[tablaEmpleados["cargo"]=="analista2"].head(50)

# Exportar tabla
archivoHTML = tablaAnalistas2.to_html()
#abrir archivo
ArchivoTEXTO = open("datosanalista2.html","w",encoding="UTF-8")
#escribir en el archivo
ArchivoTEXTO.write(archivoHTML)
#cerrar archivo
ArchivoTEXTO.close()

# filtro 3 quiero obtener todos los datos de analistas menores de 30 años y que ganan mas de 5500000
tablaAnalistas3 = tablaEmpleados[(tablaEmpleados["edad"]< 30) & (tablaEmpleados["salario"]>5500000)].head(10)
#tablaFiltro=tablaEmpleados[(tablaEmpleados["edad"]<30) & (tablaEmpleados ["salario"]>5500000)]
print(tablaAnalistas3)

# Exportar tabla
archivoHTML = tablaAnalistas3.to_html()
#abrir archivo
ArchivoTEXTO = open("datosanalista3.html","w",encoding="UTF-8")
#escribir en el archivo
ArchivoTEXTO.write(archivoHTML)
#cerrar archivo
ArchivoTEXTO.close()
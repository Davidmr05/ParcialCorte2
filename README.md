# Parcial Segundo Corte - David Esteban Martinez RIos

Punto 1:

Requisitos

Antes de empezar, asegúrate de tener los siguientes requisitos instalados:

    Python 3 (versión 3.6 o superior)
    ANTLR 4.13.2 (descargar el archivo antlr-4.13.2-complete.jar desde ANTLR)

Configura ANTLR:

Asegúrate de que ANTLR esté configurado correctamente. En tu terminal, agrega lo siguiente a tu CLASSPATH:

export CLASSPATH=".:/path/to/antlr-4.13.2-complete.jar:$CLASSPATH"

alias antlr4='java -jar /path/to/antlr-4.13.2-complete.jar'

alias grun='java org.antlr.v4.gui.TestRig'

Reemplaza /path/to/ con la ruta donde descargaste antlr-4.13.2-complete.jar.

Instala ANTLR para Python:

Instala la librería de tiempo de ejecución de ANTLR para Python con el siguiente comando:

    pip install antlr4-python3-runtime

Generar Archivos de ANTLR

Una vez que ANTLR esté configurado, compila la gramática utilizando el siguiente comando en la terminal:


antlr4 -Dlanguage=Python3 -visitor OpComplejas.g4

Este comando generará los archivos necesarios (OpComplejasLexer.py, OpComplejasParser.py, y OpComplejasVisitor.py) a partir del archivo OpComplejas.g4.
Ejecutar el Programa

    Configura el archivo de entrada:

    Crea un archivo llamado input.txt en el mismo directorio del proyecto con el siguiente contenido de ejemplo:

    txt

(2 + 7i) + (3 - 4i)
(1 + 2i) * (2 - 3i)
(4 + 5i) / (2 + 3i)
(7 - 8i) - (5 + 6i)

Ejecuta el programa:

Finalmente, puedes ejecutar el script Python para procesar el archivo de entrada input.txt:

python3 calCompleja.py

EN el caso de que el .py genere error tendriamos que usar un entorno virtual de python: 

 python3 -m venv venv

 source venv/bin/activate

 pip install antlr4-python3-runtime

 La ejecucion con el input de ejemplo deberia ser asi: 

El resultado de la operación es: 5.0 + 3.0j

El resultado de la operación es: 8.0 + 1.0j

El resultado de la operación es: 1.77 -0.15j

El resultado de la operación es: 2.0 -14.0j


Punto 2: 

  - antlr4 -Dlanguage=Python3 -visitor function.g4 
    
  - python3 main.py

La ejecucion con el input de ejemplo deberia ser asi: 

['a', 'a', 'e', 'a']

[1, 8, 27, 64]

[4, 2]

Punto 3: 

  - antlr4 -Dlanguage=Python3 -visitor fourier.g4
    
  - python3 main.py

La ejecucion con el input de ejemplo deberia ser asi: 

La transformada de fourier para esta funcion sigue la forma: 1/(jπf)

La transformada de fourier para esta funcion sigue la forma: 1/(jw) + (jπf)


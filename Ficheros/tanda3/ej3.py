"""
3. Haz un programa que reciba como parámetro un fichero encriptado con el método César, lo desencripte y almacene el
resultado en otro archivo, que también pasamos como parámetro, de manera que:

Si el programa no recibe el número de parámetros adecuado termina con un error 1.

Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que lee, pero antes
advertirá al usuario de que machacará el archivo origen, dando opción a que la operación no se haga.

Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de error y código
2.

Si en el fichero destino no se puede escribir (da error al abrirlo como escritura) el programa termina con un mensaje
de error y código 3.

Para desencriptar necesitas una clave que debes pedir al usuario.

¿Se te ocurre alguna forma de desencriptar este archivo sin pedir clave? Coméntala, y si te atreves... ¡impleméntala!

Author: Alberto Pérez Bernabeu
"""
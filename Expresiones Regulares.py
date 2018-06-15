
# coding: utf-8

# In[1]:


import re # Importamos el modulo regex


# In[12]:


# El metodo mathc determina si la expresión regular tienen coincidencias
# en el comienzo del texto

def coincidencias(text1, text2):
    if re.match(text1, text2):
        return True
    else:
        return False
    
coincidencias("Python", "Python")


# In[18]:


# Con expresiones regulares, podremos buscar todo tipo de patrones
# Por ejemplo, podremos iltrar las palabras con acentos
patron = ('\w*[ñáéíóúÑÁÉÍÓÚ]\w*')
palabras = re.compile(patron)
palabras.findall("Niño, Acción, Perro, Lobo, Expresión, Español")


# In[21]:


# Podemos utilizar las expresiones regulares para la validación de URL

#Este serie el patron que sigue una URL
url = re.compile(r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$")

if url.search("http://pythondiario.com/"): # Comprobemos que esta es una URL valida
    print("URL Valida")
else:
    print("URL No Valida")


# In[32]:


# Uno de los usos que más se le dan a las expresiones regulares
# es la verificación de correos electronicos
patron = re.compile(r"[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}")

if patron.search("pythondi1io@gmail.com"): # Comprobemos sí este es un correo electronico valido
    print("Correo valido!")
else:
    print("Correo Invalido!")


# In[33]:


fecha = re.compile(r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/((19|20)\d\d)$')

if fecha.search("13/02/1982"):
    print("Fecha Valida!")
else:
    print("Fecha Invalida!")


# In[34]:


if fecha.search("332/49/1982"):
    print("Fecha Valida!")
else:
    print("Fecha Invalida!")


#This is a multilanguage test code
# Documentación utilizada para esta prueba: https://python-para-impacientes.blogspot.com/2017/11/internacionalizacion-del-codigo-y-ii.html

import gettext
import os

ruta = os.path.dirname(os.path.realpath(__file__)) + '\locale'

idiomas = ['es_ES']
langs = gettext.translation('sample_app', 
                            ruta, 
                            languages=idiomas, 
                            fallback=True,)
_ = langs.gettext

print ("*** This is a multilanguage test file *** ")
print (_("Translated text"))

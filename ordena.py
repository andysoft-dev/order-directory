#from PIL import Image
import os
import sys, getopt
import random

downloadsFolder = "c:/Users/andyj/Downloads/"
todos = False
exte = "Ninguna"
argumentos = sys.argv

lista_de_argumentos = argumentos[1:]
short_options = "r:e:t"
long_options = ["ruta", "extension", "todas"]


#print("Buscando archivos %s" % (sys.argv[0]))

try:
    arguments, values = getopt.getopt(lista_de_argumentos, short_options, long_options)
except getopt.error as err:
    print (str(err))
    sys.exit(2)


for current_argument, current_value in arguments:
    if current_argument in ("-r", "--ruta"):
        downloadsFolder= current_value
    elif current_argument in ("-e", "--extension"):
        exte = current_value
    elif current_argument in ("-t", "--todos"):
        todos = True

print (("Ruta %s") % downloadsFolder)
print (("Extension %s") % exte)
print (("Todos %s") % todos)

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        es_archivo =os.path.isfile(downloadsFolder + filename)
        #print(es_archivo)

        #print ("pasa aca")
        name, extension = os.path.splitext(downloadsFolder + filename)
        if todos==True:
            #print ("pasa por aca")
            PDFolder = downloadsFolder + "/" + extension[1:] + "/"
            try:
                os.mkdir(PDFolder)
            except FileExistsError:
                pass

            from os.path import exists

            file_exists = exists(downloadsFolder + filename)
            if file_exists ==True and es_archivo==True:
                filename2 =  str(random.randint(0,100000)) + "_" + filename

            else:
                filename2 = filename


            os.rename(downloadsFolder + filename, PDFolder + filename2)
            if  es_archivo ==True:
                print ((filename + " movido a %s") % extension[1:])

        elif extension in [exte]:
            PDFolder = downloadsFolder + "/" + exte[1:] + "/"
            try:
                os.mkdir(PDFolder)
            except FileExistsError:
                pass

            from os.path import exists
            file_exists = exists(downloadsFolder + filename)
            if file_exists ==True and es_archivo==True:
                filename2 =  str(random.randint(0,100000)) + "_" + filename
            else:
                filename2 = filename

            os.rename(downloadsFolder + filename, PDFolder + filename2)
            if es_archivo ==True:
                print (filename + " movido a " + exte[1:])


import fileinput
import re
import fitz
import collections
import spacy
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

nlp = spacy.load("es_core_news_sm") 

class archivo ():
    def __init__(self, direccion_archivo, archivo_nuevo):
        self.direccion_archivo = direccion_archivo
        self.archivo_nuevo = archivo_nuevo
        self.text = self.readPDF()
        self.token = []
        self.frecuencia = {}
        
    def readPDF (self):
        
        doc = fitz.open(self.direccion_archivo)
        self.text = ""
        for page in doc:
            self.text += page.getText()
    
    def imprimir_archivo(self):    
        print(self.text)
        open('archivo_nuevo.txt', 'w').write(self.text)
        
    
    #funcion leer archivo y crear otro para modificar
    #string = open('DocModificable').read()
    #open('DocModificable', 'w').write(string)
    
    #remove special characters
    def remove_Special_Characters (self):
    
        string = open('archivo_nuevo.txt').read()
        result = re.sub('[^a-zA-Z0-9\n\.]', '', string)
        open('archivo_nuevo.txt', 'w').write(result)
        #print (result)
    
    #funcion quitar numeros
    def remove_Numbers (self):
        
        for line in fileinput.input("archivo_nuevo.txt", inplace=True):
            result = ''.join(i for i in line if not i.isdigit())
            print (result)
        
    
    #borrar espacios en blanco multiples
    def remove_Blank_Spaces (self):
        
        string = open('archivo_nuevo.txt').read()
        result = re.sub(' +', ' ', string )
        open('archivo_nuevo.txt', 'w').write(result)
    
    def raiz_de_palabras(self):
        tokens = nlp(self.text)
        for word in tokens:
            self.text = " ".join([word.lemma_ for word in tokens])
    
    def eliminar_stop_words(self):
        self.text = self.text.lower()
        temp = self.text.split()
        for word in temp:
            if word not in stopwords.words("spanish"):
                self.token.append(word)

    def imprimir_token(self):
        for word in self.token:
            print(word)          
       
    def contador(self):
        self.frecuencia = collections.Counter(self.token)
     
texto = archivo("peterpan.pdf", 'DocModificable.txt')
texto.readPDF()
texto.imprimir_archivo()
texto.remove_Special_Characters()
texto.remove_Numbers()
texto.raiz_de_palabras()
texto.eliminar_stop_words()
print('/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
print('\nTexto modificado\n')
texto.imprimir_token()
texto.contador()
print('/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
print('\nFrecuencia de palabras\n')
print(texto.frecuencia)
print('Fin')
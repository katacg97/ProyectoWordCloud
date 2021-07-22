import fileinput
import re
import fitz
import collections
import spacy
import nltk
import pandas as pd
import csv
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from pandas import DataFrame
from collections import Counter
import threading
import time
#from prueba2 import myThread
from test.test_tools.test_unparse import for_else
nltk.download('stopwords')

nlp = spacy.load("es_core_news_sm") 

class archivo ():
    def __init__(self, direccion_archivo, archivo_nuevo):
        self.direccion_archivo = direccion_archivo
        self.archivo_nuevo = archivo_nuevo
        self.token = []
        self.frecuencia = {}
        self.textoATrabajar=""
        
    def readPDF (self, threadID):
        
        doc = fitz.open(self.direccion_archivo)
        self.textoA = ""
        self.textoB = ""
        paginas= doc.page_count
        mitad_doc= round(paginas/2)
        i = 0
        
        for page in doc:
            if i <mitad_doc:
                self.textoA += page.getText()
            else:
                self.textoB += page.getText() 
            i+=1
            
          
    def imprimir_archivo(self):    
        print(self.textoATrabajar)
        open('archivo_nuevo.txt', 'w').write(self.textoATrabajar)
        
    
    #funcion leer archivo y crear otro para modificar
    #string = open('DocModificable').read()
    #open('DocModificable', 'w').write(string)
    
    #remove special characters
    def remove_Special_Characters (self):
    
        #string = open('archivo_nuevo.txt').read()
        result = re.sub('\!|\'|\?|\-|\.|\,|\:', '', self.textoATrabajar)
        #open('archivo_nuevo.txt', 'w').write(result)
        self.textoATrabajar=result       
        #print (result)
   
    #funcion quitar numeros
    def remove_Numbers (self): 

        pattern = r'[0-9]'

        string = re.sub(pattern, '', self.textoATrabajar)
        self.textoATrabajar=string

          
    #borrar espacios en blanco multiples
    def remove_Blank_Spaces (self):
        
        string = open('archivo_nuevo.txt').read()
        result = re.sub(' +', ' ', self.textoATrabajar )
        #open('archivo_nuevo.txt', 'w').write(result)
        self.textoATrabajar=result
    
    def raiz_de_palabras(self):
        tokens = nlp(self.textoATrabajar)
        for word in tokens:
            self.textoATrabajar = " ".join([word.lemma_ for word in tokens])
    
    def eliminar_stop_words(self,threadID):
        self.textoATrabajar = self.textoATrabajar.lower()
        temp = self.textoATrabajar.split()
        for word in temp:
            if word not in stopwords.words("spanish"):
                self.token.append(word)
        
        if threadID==1:
            self.tokenA=self.token
            
        else :
            self.tokenB=self.token

    def imprimir_token(self):
        for word in self.token:
            print(word)          
       
    def contador(self):
        print(type(self.token))
        print(type(self.tokenA))
        print(type(self.tokenB))
        self.token = self.tokenB+self.tokenA
        #self.token.extend(self.tokenA)
        self.frecuencia = collections.Counter(self.token)  
        #self.imprimir_token()
        print(type(self.token))
        
      
    def lista_a_DataFrame(self):
        
        c = Counter(self.frecuencia)
        self.dataFrameDefinitivo = pd.DataFrame.from_records(list(dict(c).items()), columns=['Palabra','Contador'])
        self.dataFrameDefinitivo.set_index('Palabra', inplace = True)
        print(self.dataFrameDefinitivo)
        
    def proceso_Completo(self, threadID):
        
        
        
        #112 y 113 van a ir en el main
        #texto = archivo("peterpan.pdf", 'DocModificable.txt')
        self.readPDF(threadID)
        
        if threadID==1:
            self.textoATrabajar = self.textoA
            
        else :
            self.textoATrabajar= self.textoB
        
        #texto.imprimir_archivo()
        texto.remove_Special_Characters()   
        texto.remove_Numbers()
        texto.remove_Blank_Spaces()
        texto.raiz_de_palabras()
        texto.eliminar_stop_words(threadID)
        
           
    def Word_Cloud(self):
        wordcloud = WordCloud()
        wordcloud.generate_from_frequencies(frequencies=self.frecuencia)
        
        # plot the WordCloud image                      
        plt.figure(figsize = (8, 8), facecolor = None)
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.tight_layout(pad = 0)
         
        plt.show()
        
class myThread (threading.Thread):
    
    def __init__(self, threadID, name, counter,objeto):
        self.objeto=objeto
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
      
    def run(self):
        print ("Starting " + self.name)
        #print_time(self.name, 5, self.counter)
        self.objeto.proceso_Completo(self.threadID)
        
        print ("Exiting " + self.name)   
        
        
        
        
        


texto = archivo("peterpan.pdf", 'DocModificable.txt')
#texto.readPDF()

# Create new threads
#(threadID, name, counter)
thread1 = myThread(1, "Parte 1", 1, texto)
thread2 = myThread(2, "Parte 2", 2, texto)
"""
thread1 = myThread("Parte 1", 1)
thread2 = myThread("Parte 2", 2)
"""

# Start new Threads
thread1.start()
thread2.start()

thread1.join()
thread2.join()


#print('Data Frame')
#texto.lista_a_DataFrame()

texto.contador()
print('/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
print('\nFrecuencia de palabras\n')
print(texto.frecuencia)
texto.Word_Cloud()

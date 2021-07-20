import nltk
import fileinput
import re
import fitz 

class archivo ():
    def __init__(self, direccion_archivo, archivo_nuevo):
        self.direccion_archivo = direccion_archivo
        self.archivo_nuevo = archivo_nuevo
        self.text = self.readPDF()
        
    def readPDF (self):
        
        doc = fitz.open(self.direccion_archivo)
        self.text = ""
        for page in doc:
            self.text += page.getText()
    
    def imprimir_archivo(self):    
        print(self.text)
        open('self.archivo_nuevo', 'w').write(self.text)
        
    
    #funcion leer archivo y crear otro para modificar
    #string = open('DocModificable').read()
    #open('DocModificable', 'w').write(string)
    
    #remove special characters
    #def removeSpecialCharacters ():
    """
    string = open('DocModificable.txt').read()
    result = re.sub('[^a-zA-Z0-9\n\.]', ' ', string)
    open('DocModificable.txt', 'w').write(result)
    print (result)
    
    #funcion quitar numeros
    #def removeNumbers ():
    for line in fileinput.input("DocModificable.txt", inplace=True):
    
    #remove digits
        result = ''.join([i for i in line if not i.isdigit()])
        #print (DocModificable.txt)
        
     """
texto = archivo("a.pdf", 'DocModificable.txt')
texto.readPDF()
texto.imprimir_archivo()

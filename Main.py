import fileinput
import re
import fitz 



class archivo ():
    #def readPDF (self):
        
    with fitz.open("a.pdf") as doc:
        text = ""
        for page in doc:
            text += page.getText()
    
    print(text)
    open('DocModificable.txt', 'w').write(text)
    
    
    #funcion leer archivo y crear otro para modificar
    #string = open('DocModificable').read()
    #open('DocModificable', 'w').write(string)
    
    #remove special characters
    #def removeSpecialCharacters ():
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
        
        

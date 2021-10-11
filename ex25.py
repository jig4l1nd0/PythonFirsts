# - - coding: utf- 8 - - 
def break_words(stuff):
    """Vamos a partirpalabras"""
    Worter = stuff.split(" ") 
    return Worter

def sort_words(Worter):
    """Ordena las palabras"""
    return sorted(Worter)
    
def print_first_word(Worter):
    '''imprime la primera palabra'''
    Wort = Worter.pop(0)
    print Wort
    
def print_last_word(words):
    '''Imprime la última palabra'''
    word = words.pop(-1)
    print word
    
def sort_sentence(sentence):
    '''Toma una oración completa y la regresa como una lista ordenada'''
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    '''Imprime la primera y la ultima palabra de la oración'''    
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    '''Imprime la primera y la última pero con la lista ordenada'''
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
            
    
        

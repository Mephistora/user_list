#Funciones 

import re
from os import system, name


def validate_name(user_name):
    """
    Función que permite validar el nombre de usuario

    Parameters
    ----------
    user_name : str

    Returns
    -------
    bool
    """
    
    if user_name.isalpha() and len(user_name) < 30 and user_name != "":
        return True
    else:
        return False

def validate_password(user_password):
    '''
    función que permite validar la contraseña 
    ------------
    Parameters
    --------------------
    user_password : str
    --------------------
    returns
    -------------------
    bool
    '''
    if len(user_password) >= 8:
        return True
    else:
        return False

def clear():
    '''
    funsión que permite limpiar la consola
    '''
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


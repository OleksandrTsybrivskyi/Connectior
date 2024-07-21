import re

# Email verification
# Password verification
# First name verification
# Last name verification
# Nickname verification

def verify_email(email) -> bool:
    '''
    Email must be: email@email.domen
    '''
    return re.match(r'[^@]+@[^@]+\.[^@]+', email)

def verify_password(password: str) -> bool:
    '''
    Password must:
    - be at least 6 characters long and at most 30 characters long
    - contain only:
    > + letters,
    > + numbers,
    > + special characters: ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~
    '''
    return re.match(r'^[A-Za-z\d!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~]{6,30}$', password)

def verify_first_name(first_name: str) -> bool:
    '''
    First name must be at least 1 character long and at most 16 characters long
    '''
    return re.match(r'^(?=.*\S).{1,16}$', first_name)

def verify_last_name(last_name: str | None) -> bool:
    '''
    Last name can be None or at least 1 character long and at most 16 characters long
    '''
    if last_name == None:
        return True
    
    return re.match(r'^(?=.*\S).{1,16}$', last_name)

def verify_nickname(nickname: str) -> bool:
    '''
    Nickname must:
    - be at least 4 character long and at most 16 characters long
    - contain only:
    > + letters,
    > + numbers,
    > special characters: - _ .
    - not contain any spaces
    '''
    return re.match(r'^[A-Za-z\d._-]{4,16}$', nickname)


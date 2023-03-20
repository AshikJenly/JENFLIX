import random
import string

def generate_confusion_data():
    alphabet = string.ascii_uppercase+string.ascii_lowercase + string.digits+"!@#$%^&*><. "
    confusion_data = ''.join(random.sample(alphabet, random.randint(15,25)))
    
    return confusion_data

def alter_encrypted_value(encrypted_value,confusion_data):
   
    confusion_data=confusion_data+str(len(confusion_data))
    
    left=encrypted_value[:int(len(encrypted_value)/2)]
    right=encrypted_value[int(len(encrypted_value)/2):len(encrypted_value)]
    
    l_len=str(len(left))
    r_len=str(len(right))
    
    l_l_len=str(len(l_len))
    l_r_len=str(len(r_len))

    
    left=left+r_len+l_r_len
    right=right+l_l_len+l_len
    
    
    encrypted_value=right+confusion_data+left
    
    
    
    return encrypted_value

def realter_encrypted_value(encrypted_value):
    digit_right=int(encrypted_value[-1:])
    encrypted_value=encrypted_value[0:-1]
    
    len_right=int(encrypted_value[-digit_right:])
    
    encrypted_value=encrypted_value[:-digit_right]
    
    digit_left=int(encrypted_value[len_right])
    len_left=int(encrypted_value[len_right+1:len_right+1+digit_left])
    
    real_value_left=encrypted_value[-len_left:]
    real_value_right=encrypted_value[0:len_right]
    
    real_encrypted_data=real_value_left+real_value_right
    
    return real_encrypted_data

def get_enckey():
    alphabet = string.ascii_uppercase+string.ascii_lowercase + string.digits+"!@#$%^&*><. "
    encryption_key = ''.join(random.sample(alphabet, len(alphabet)))

    return encryption_key

def encryption(txt,encryption_key):
    alphabet = string.ascii_uppercase+string.ascii_lowercase + string.digits+"!@#$%^&*><. "
    encryption_map = dict(zip(alphabet, encryption_key))
    encrypted_value=''.join((encryption_map.get(char) for char in txt))
    
    
    encrypted_value=alter_encrypted_value(encrypted_value,generate_confusion_data())
    
    return encrypted_value

def decryption(txt,key):
    
    txt=realter_encrypted_value(txt)
    alphabet = string.ascii_uppercase+string.ascii_lowercase + string.digits+"!@#$%^&*><. "

    decryption_map = dict(zip(key,alphabet))
    decryption_value=''.join((decryption_map.get(char) for char in txt))
    
    return decryption_value
from .models import UserInfoDB1
from .DataSecurity import decryption

def checkLogin(email,password):
    objs=UserInfoDB1.objects.all()
    for obj in objs:
        key=obj.key_enc
        if decryption(obj.email,key)==email:
            if decryption(obj.password,key)==password:
                return None,True
            else:
                return "Wrong Password ,Please try again!",False
        
    return "Sorry,User does'nt exist please register.",False    
    
def checkRegister(email):
    objs=UserInfoDB1.objects.all()
    for obj in objs:
        key=obj.key_enc
        if decryption(obj.email,key)==email:
            return True
        
    return False    
    
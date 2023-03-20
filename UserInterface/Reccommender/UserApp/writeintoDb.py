
from .models import UserInfoDB1
from .DataSecurity import encryption,get_enckey

def writeIntoDB(uf):
    print("----------DB WRITE-----------")

    enc_key=get_enckey()
    fname=encryption(uf.fname,encryption_key=enc_key)
    lname=encryption(uf.lname,encryption_key=enc_key)
    email=encryption(uf.email,encryption_key=enc_key)
    college=encryption(uf.college,encryption_key=enc_key)
    password=encryption(uf.password,encryption_key=enc_key)

    user_info= UserInfoDB1(fname=fname, lname=lname,email=email,college=college,password=password,key_enc=enc_key)
    user_info.save()
    print("----------DB WRITE-----------")


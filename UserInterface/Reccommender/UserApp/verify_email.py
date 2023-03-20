
import smtplib
import random
my_email ="jenlyjosephkarter@gmail.com"
pass_word = "qmtuovzlqzpwgwct"
# gmail
# qmtuovzlqzpwgwct
# yahoo
# IKUCHA6V7VBQSCLYZNJAME3MQ7ZTNKNM
class MailVerify:
    def __init__(self):
       pass

    def verifyOtp(self,email,name):
        
        
        try:
                self.__connection = smtplib.SMTP("smtp.gmail.com")
                self.__connection.starttls()#tls is transport layer security
                self.__connection.login(user=my_email,password=pass_word)
                otp=""
                for i in range(6):
                    otp +=str(random.randint(0,9))
                self.__connection.sendmail(from_addr=my_email,to_addrs=email,msg=f"Subject:JENFLIX OTP\n\nDear {name}\nThank you for registering\n\nyour otp is {otp}.")
                self.__connection.close()
        except:
            otp="739706"
            print('Error Occured in sending mail')
            return otp


# m1=MailVerify()
# x=m1.verifyOtp('jenlyashik@gmail.com',"ashik")
# print(x)


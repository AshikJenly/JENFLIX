
class UserInfo:
    def __init__(self) -> None:
        pass

    def values(self,fname,lname,email,college,password):
        self.fname=fname
        self.lname=lname
        self.email=email
        self.college=college
        self.password=password
    def set_otp(self,otp):
        self.__otp=otp
    def check_otp(self,check):
        if check == self.__otp:
            return True
        else:
            return False
# Декораторы staticmethod и classmethod
class User():

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @staticmethod
    def is_valid_email(email):
        if '@' in email:
            return True
        else:
            return False
    
    @classmethod
    def create_anonymous(cls):
        return cls(name = 'Anonymous', email = '')
    
print(User.is_valid_email('test@email.com'))
usr = User.create_anonymous()
print(usr.name)
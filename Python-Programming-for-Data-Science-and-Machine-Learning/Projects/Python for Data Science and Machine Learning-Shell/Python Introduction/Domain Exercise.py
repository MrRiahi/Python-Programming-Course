
def DomainGet(email):
     return email.split('@')[1]


email = 'user@domain.com'
print(DomainGet(email))


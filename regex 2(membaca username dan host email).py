import re

#pakai fungsi split dari string 
def proses_email(email): #harus return tuple (username, host)
    email_split= email.split('@')
    return (email_split[0], email_split[1])

def proses_email_regex(email): 
    pattern= r"(.+)@(.+)" #ambil semua yang dipisahkan @ 
    hasil= re.search(pattern, email)
    #outputnya seperti apa 
    print(hasil)
#input user 
email= input('Masukkan alamat email yang valid: ')
hasil= proses_email(email)

print(f'username: {hasil[0]}')
print(f'hostname: {hasil[1]}')

hasil= proses_email_regex(email)
print(f'username: {hasil[0]}')
print(f'hostname: {hasil[1]}')
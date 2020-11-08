from getpass import getpass
import os
import time
os.system('clear')
print('\033[1;31m[ Login ]')
print("")
print("")
print("")
x = raw_input('\x1b[1;33m[ Username/ID ]~> \x1b[1;36m')
print("")
e = getpass('\x1b[1;33m[ Password ]   ~> \x1b[1;36m')

if x=="3mweCyb3r56" and e=="emwe56":
   print('Username Dan Password \x1b[1;32mBENAR')
   time.sleep(3)
   os.system('bash test.sh')
else:
   print('Mohon Maaf Login Gagal')
   print('Silahkan Hubungi Author Untuk Username Dan Password')
   os.system('xdg-open https://api.whatsapp.com/send?phone=6285956067789&text=Hai%20Author,%20saya%20minta%Username%20dan%20IDnya%20dong')
   time.sleep(5)
   os.system('exit')

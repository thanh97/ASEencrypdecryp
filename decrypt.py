import sys
import getpass
import project_aes

password = getpass.getpass('password> ')
dec = project_aes.decrypt(sys.stdin.buffer.read(), password)
sys.stdout.buffer.write(dec)
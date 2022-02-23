import os

print('installing pip.....')
os.system('sudo apt install python3-pip -y')
print('installing required packages')
os.system('pip3 install -r requirements.txt')

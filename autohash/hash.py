#!/usr/bin/python3

print(" ▄▄    ▄▄                      ▄▄                           ")       
print(" ██    ██                      ██                           ")
print(" ██    ██   ▄█████▄  ▄▄█████▄  ██▄████▄   ▄████▄    ██▄████ ") 
print(" ████████   ▀ ▄▄▄██  ██▄▄▄▄ ▀  ██▀   ██  ██▄▄▄▄██   ██▀     ")
print(" ██    ██  ▄██▀▀▀██   ▀▀▀▀██▄  ██    ██  ██▀▀▀▀▀▀   ██      ")
print(" ██    ██  ██▄▄▄███  █▄▄▄▄▄██  ██    ██  ▀██▄▄▄▄█   ██      ")
print(" ▀▀    ▀▀   ▀▀▀▀ ▀▀   ▀▀▀▀▀▀   ▀▀    ▀▀    ▀▀▀▀▀    ▀▀      ")
                                                            

print("pemmision")
print(" ")
print("1.hashdeep")
print(" ")

print('only linux')
print(" ")
print("hash by md5")
print(" ")
print(" ")
print("by ckedtsu")
print(" ")
print(" ")
import os
import random

result = random.random()

os.system('mkdir c')
os.system('mkdir hash')


what1 = input("your text: ")
os.system('echo ' + what1 + ' > c/0.dat')
os.system('md5deep c/0.dat')
hash1 = input('yor hash: ')
os.system('echo ' + hash1 + ' > hash/'+ str(result) + '.dat')
os.system('rm c/0.dat') 
os.system('cat hash/' + str(result) + '.dat')

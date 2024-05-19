import cv2
import os
import string

img = cv2.imread("flower.jpg")
msg = input("Enter secret message")
password = input("Enter a passcode")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m, n, z = 0, 0, 0


for i in range(len(msg)):
    img[n,m,z] = d[msg[i]]
    n += 1
    m += 1
    z = (z+1)%3 

cv2.imwrite("encryptedimage.jpg",img)

os.startfile("encryptedimage.jpg")

message = ""
n, m, z = 0, 0, 0

pas = input("Enter passcode for Decryption")
if password == pas:
    for i in range(len(msg)):
        message = message+ c[img[n,m,z]]
        n += 1
        m += 1
        z = (z+1)%3
    print("Decrypted message = ",message)
else:
    print("You are not authenticated")

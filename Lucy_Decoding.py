#!/usr/bin/env python
import sys
import os

encoded_jpg_name = 'Lucy_Encoded.jpg'

input_jpg = open(encoded_jpg_name, 'r')
input_encoded = input_jpg.read().encode('base64')

### You may see some hidden message. 
print(input_encoded)

### 
print('\n')
print('You may see a hidden message')

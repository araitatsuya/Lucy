#!/usr/bin/env python
import sys
import os

input_jpg_name = 'Lucy.jpg'
encoded_jpg_name = 'Lucy_Encoded.jpg'

input_jpg = open(input_jpg_name, 'r')
output_jpg = open(encoded_jpg_name, 'w')

## Read file and Encode
input_encoded = input_jpg.read().encode('base64')

## Input Message
print("Input Message: ")
message_embedded = raw_input()
## e.g. Lucy is plotting something. 

output_encoded = input_encoded[:-3] + message_embedded + '000=='
print(output_encoded)

## Decode and Write file
output_jpg.write(output_encoded.decode('base64'))

'''
### Str Swap ###
#l_message_embedded  = list(message_embedded + '==')
#l_output_encoded  = list(input_encoded)
#l_output_encoded = l_output_encoded
#print(l_output_encoded)
#for x in range(0, len(l_message_embedded) + 1):
#	l_output_encoded[-x] = l_message_embedded[-x]
#output_encoded = ''.join(l_output_encoded )
'''
import string

text = input('Digite seu texto:\n')

print(text.translate(bytes.maketrans(b'aeiots',b'43!07$')))

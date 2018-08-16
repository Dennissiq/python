text = input("Digite seu texto: ")

leetmsg = text

leetwords = "aeiots"
for letter in text:
    if letter in leetwords:
        leetmsg = leetmsg.replace('a', str(4))
        leetmsg = leetmsg.replace('e', str(3))
        leetmsg = leetmsg.replace('i', '!')
        leetmsg = leetmsg.replace('o', str(0))
        leetmsg = leetmsg.replace('t', str(7))
        leetmsg = leetmsg.replace('s', '$')

print("Seu texto l33t é:", leetmsg.upper())

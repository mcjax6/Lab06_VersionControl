
def encode(password):

    encrypted = ""
    for x in password:

        temp = int(x) + 3
        encrypted = encrypted + str(temp)

    return encrypted
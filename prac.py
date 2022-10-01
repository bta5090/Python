

def coins(cent, nick, dime, quart):

    cent = float(cent)
    nick = float(nick)
    dime = float(dime)
    quart = float(quart)
    
    register = 50
    c = 0.01
    n = 0.05
    d = 0.1
    q = 0.25

    if ((cent or nick or dime or quart)) != 0:

        register += (cent*c) + (nick*n) + (dime*d) + (quart*q)
        print("\nRegister has a current deposit of $",register, "\n")

    else:
        print("\nNo coins were deposited. Current register contains $",register, "\n")


coins(input(), input(), input(), input())
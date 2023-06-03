
i=1

resp = 's'
while resp == 's':
    m = int(input ("qual  tabuada?"))
    while i<=10:
        print (m, "x", i, "=", m * i)
        i=i+1
        # i ta valendo 11
    resp = input ("Deseja uma nova tabuada? [s]im [n]ão ")
    i=1
    print ("-" * 40)

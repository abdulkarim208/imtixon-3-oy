sonlar = [12, 7, 5, 18, 9, 4]

def tahlil_qil(sonlar):
    juft = 0
    toq = 0

    for son in sonlar:
        if son % 2 == 0:
            juft += son
        else:
            toq += son

    print("Juft sonlar yig'indisi:", juft)
    print("Toq sonlar yig'indisi:", toq)
    print("Eng katta son:", max(sonlar))

tahlil_qil(sonlar)
def notas(*n, sit=False):
    r = dict()
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["média"] = sum(n)/len(n)
    if sit == True:
        if r["média"] >= 7:
            r["situação"] = 'Boa'
        elif r["média"] >=5:
            r["situação"] = 'Razoável'
        else:
            r["situação"] = 'Ruim'
    return r


#Programa Principal
resp = notas(4, 5, 8, 8, sit=True)
print(resp)
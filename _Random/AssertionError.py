def KtoF(temper):
    assert (temper>=0),"Colder than absoluter zero"
    return ((temper-273)*1.8)+32
print(KtoF(273))
print(KtoF(-8))

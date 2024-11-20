def caracinf(primtex: str, segtex: str) -> list:
    carac = []

    if len(primtex) == len(segtex):
        for index in range(0, len(primtex)):
            if primtex[index] != segtex[index]:
                carac.append(segtex[index])

    return carac

print(caracinf("esnupi plaza", "esnup1 wlaza"))  
print(caracinf("plaza ronaldo", "plaza r0naldo"))  
print(caracinf("plaza ronaldo", "plaza roanldo"))  
print(caracinf("davidfoc", "dav1dfoc"))  

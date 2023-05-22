

fucking_dictinaty = {'dick': ["suka", "bliat"], "hui": "poshol_nach"}

for bliat, suka in fucking_dictinaty.items():
    print(bliat)
    if isinstance(suka, list):
        for pes in suka:
            print(pes)
    else:
        print(suka)
        print("ujebok")

for value in fucking_dictinaty.values():
    print(value)
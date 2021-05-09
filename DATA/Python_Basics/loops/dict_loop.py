test = {
    "annu": {
        'nr': 345436456,
        "city": "Rapla"
    },
    "mati": {
        'nr': 345436456,
        "city": "Saue"
    },
    "silver": {
        'nr': 345436456,
        "city": "Tallinn"
    },
}

for i in test:
    for key,value in test[i].items():
        print(value)
capitales = {
    'EE UU': 'Washington',
    'Argentina': 'Buenos aires',
    'Chile': 'Santiago',
    'Venezuela': 'Caracas',
    'Cursos': ['Python', 'Javascrit', 'React'],
    'Año': 2024,
    'Activo': True
}

capitales.update({
    'Alemania': 'Berlin'
})
#capitales.pop('EE UU')
#capitales.clear()

#print(capitales)
#print(capitales.get('Chile'))
#print(capitales.keys())
#print(capitales.values())
#print(capitales.items())

for key, value in capitales.items() : print(key, value)



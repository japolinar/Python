utensilios = {'tenedor', 'cuchara', 'cuchillo'} #<<-- los {} son sets
platos = {'plato', 'bol', 'taza'}

#utensilios.add('cucharon')
#utensilios.remove('tenedor')
#utensilios.pop()
#utensilios.clear()
#print(utensilios.difference(platos))
#print(utensilios.intersection(platos))

utensilios.update(platos)

for i in utensilios : print(i)
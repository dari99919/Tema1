def ordenar(c):
    return c['prioridad']
cola = [
    {'tarea2' : 'saltar', 'prioridad' : '2'},
    {'tarea1' : 'correr', 'prioridad' : '1'}
    {'tarea4' : 'reir', 'prioridad' : '4'}
    {'tarea3' : 'llorar', 'prioridad' : '3'}
]
cola.sort(key=ordenar)
print(cola[0]['tarea1'], cola[1]['tarea2'], cola[2]['tarea3'], cola[3]['tarea4'])

sss
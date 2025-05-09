# Retos Unidad 2

**[Video Explicación Retos U3](https://upbeduco-my.sharepoint.com/:v:/g/personal/santiago_riosd_upb_edu_co/EYxqvTtsEt9LoXMq0n1VSJgBIZjeLv0LjUaUWoWhel5jWA?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=HsOGlH)**

## Reto 1

### Descripçión del programa

Este programa gestiona la reserva de un vuelo en la aerolínea ficticia “FastFast Airlines”. Tiene en cuenta el día de la semana, el asiento preferido por el pasajero y el origen y el destino del vuelo.

### Flujo del programa

1. Se solicitan y muestran, en orden, los datos del pasajero
   1. `tit` : título de la persona.
   2. `nombre` : nombre de la persona.
   3. `apellido` : apellido de la persona.
2. Se solicitan los datos del vuelo
   1. `ciudad_o` : ciudad de origen
   2. `ciudad_d` : ciudad de destino
   3. `dia_s` : dia de la semana del vuelo
   4. `dia_m` : dia del mes del vuelo
   5. `tipo_asiento` : tipo del asiento preferido por el pasajero
3. Se calcula la distancia del vuelo, asignando un valor a la variable `dist`, según la distancia del vuelo
   1. Medellín ↔ Bogotá: 240 km
   2. Medellín ↔ Cartagena: 461 km
   3. Bogotá ↔ Cartagena: 657 km
   4. Si no es ninguna de estas rutas, se muestra un mensaje
4. Se selecciona una lista de precios, según la distancia. La lista contiene dos valores, el primero indica el precio entre semana y el segundo el precio el fin de semana.
5. Se selecciona de la lista, el precio según el día de la semana del vuelo.
6. Se genera un número aleatorio para darle un asiento al pasajero.
7. Se imprime toda la información recopilada del vuelo.

## Reto 2

### Descripción del programa

Este programa simula la desintegración de un satélite que pierde altitud en cada órbita. A medida que el satélite desciende, la fuerza de arrastre aumenta, hacieno que descienda más rápido. Finalmente, el satélite puede reingresar en la atmósfera (si su altitud llega por debajo de un mínimo seguro) o estabilizar su órbita (si la pérdida de altitud se vuelve muy pequeña).

### Flujo del programa

1. Se imprime un mensaje indicando que se inicia la simulación.
2. Se piden los datos al usuario
   1. `altitud_inicial` : Altitud con la que comienza el satélite [=] km
   2. `coef_arrastre_inicial` : Número que determina cuánto disminuye la altitud del satélite en cada órbita.
   3. `altitud_minima_segura` : Altitud por debajo de la cual se considera que el satélite reingresa en la atmósfera y se desintegra.
3. Se inicializan las variables
   1. `altitud_actual` : Se establece con el valor de `altitud_inicial`.
   2. `coef_arrastre` : Se inicializa con `coef_arrastre_inicial`.
   3. `estabilizacion` : Un valor fijo. Si el satélite pierde menos que esto, decimos que prácticamente se ha estabilizado.
   4. `orbitas` : Contador para saber cuántas órbitas ha dado el satélite.
4. Se inicia el bucle principal, se inicializa en `0`.
   1. Se aumenta el contador de órbitas.
   2. Se calcula cuánta altitud se pierde.
   3. Se resta la altitud perdida de la altitud actual.
   4. Se incrementa el coeficiente de arrastre.
   5. Se imprime información de la órbita
5. Condiciones para que termine el bucle (`while True`) y el programa
   1. Si la altitud actual es menor o igual a la altitud segura, se muestra un mensaje y se rompe el bucle.
   2. Si la cantidad de altitud que se pierde es muy pequeña, se muestra un mensaje y se rompe el bucle.

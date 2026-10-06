# Milestones

Los milestones son productos que se irán entregando durante el desarrollo del proyecto. Cada uno representa un nivel de avance sobre el problema y debe proporcionar un producto mínimamente viable sobre el que poder continuar trabajando en el siguiente.

## Milestone 0: Modelo del problema

### OBJETIVO:
Construir un programa que represente los conceptos necesarios para gestionar los contenedores, los pedidos y los viajes, teniendo en cuenta la información necesaria para conocer su situación y poder realizar posteriormente la asignación de contenedores.

### QUÉ SE ENTREGA:
Una representación de los contenedores, incluyendo toda la información necesaria para conocer su situación, ubicación. características y restricciones de uso.

Una representación de los pedidos, incluyendo la información necesaria para conocer cuándo y dónde se necesita un contenedor, las características que debe cumplir y, cuando corresponda, el contenedor que tiene asignado.

Una representación de los viajes, entendidos como pedidos que ya tienen un contenedor asociado, incluyendo la información necesaria para conocer la operación que está realizando el contenedor, su origen, destino y fechas. 

La relación entre los contenedores, los pedidos y los viajes, de forma que pueda conocerse qué contenedor está asociado a cada pedido y qué operaciones tiene pendientes.

La representación de la información diaria de los contenedores necesaria para poder conservar posteriormente su trazabilidad.

Documentación en docs/ donde se explique el modelo construido a partir de las historias de usuario y las decisiones tomadas para representar estos conceptos.

### VALIDEZ:
El milestone se considera válido cuando el modelo permite representar la información necesaria de contenedores, pedidos y viajes para comenzar a implementar la lógica de planificación y trazabilidad en el siguiente milestone.

## Milestone 1: Lógica de planificación y trazabilidad

### OBJETIVO:
Implementar la lógica necesaria para utilizar el modelo anterior y comenzar a resolver las necesidades de la responsable de logística.

### QUÉ SE ENTREGA:
#### Trazabilidad y disponibilidad
- La lógica para poder consultar la información histórica de un contenedor y conocer dónde se encontraba, su situación, la mercancía que transportaba y el viaje que tenía asociado en una fecha determinada. 

- La lógica necesaria para determinar qué contenedores pueden utilizarse para un pedido futuro teniendo en cuenta: 

-Dónde se necesitan.

-Cuándo se necesitan.

-Los viajes que ya tienen asigandos.

-La fecha en la que terminan esos viajes.

-Las características necesarias para realizar el pedido.

-Las restricciones de mercancías transportadas anteriormente.

- La lógica necesaria para identificar qué pedidos pueden ser cubiertos con la flota disponible y cuáles quedan sin cubrir.

#### Planificación de asignaciones.
Una propuesta de asignación de contenedores a los pedidos, teniendo en cuenta los viajes ya existentes y la posibilidad de aprovechar la ubicación en la que finalizan para reducir desplazamientos innecesarios de contenedores vacíos.
La posibilidad de revisar la propuesta de asignación y modificar las asignaciones cuando la responsable de logística considere que una determinada decisión no es adecuada.
Tests automatizados que permitan comprobar el comportamiento de la lógica implementada.

### VALIDEZ:
El milestone se considera válido cuando, a partir de información de contenedores, pedidos y viajes, los tests automatizados comprueban que el sistema puede:

1. Consultar la trazabilidad de los contenedores.

2. Determinar qué contenedores pueden utilizarse para un pedido.

3. Detectar los pedidos que no pueden cubrirse.

4. Proponer asignaciones teniendo en cuenta los viajes existentes y las condiciones de los pedidos.

5. Permitir modificar las asignaciones propuestas.
# Company Co — escenario sintético de atención

Estado: borrador para integración. Todos los nombres, empresas, conversaciones y hechos de este archivo son ficticios. No son registros de personas ni autorizan comunicaciones reales. Base: `USE_COMPANY_CO_INFO_FOR_DEMOS.md`, Company Co S.A.S., Bogotá, cafeterías, COP y zona America/Bogota. El escenario es una muestra operativa, no los totales comerciales anuales de Company Co.

## Catálogo de clientes

| ID | Cliente ficticio | Perfil | Interés |
|---|---|---|---|
| C001 | Café Bruma | B2B, Bogotá | Apertura de cafetería |
| C002 | Lucía Pineda | B2C, Medellín | Máquina de espresso doméstica |
| C003 | Café Nube Andina | B2B, Cali | Mantenimiento de molino |
| C004 | Mateo Cifuentes | B2C, Bogotá | Pedido y entrega |
| C005 | Tostadores del Río | B2B, Medellín | Capacitación de baristas |
| C006 | Sara Montenegro | B2C, Cali | Garantía de máquina |
| C007 | Café La Estación Azul | B2B, Bogotá | Diseño de espacio |
| C008 | Daniel Ariza | B2C, Bogotá | Devolución de producto |
| C009 | Pan y Grano Ficticio | B2B, Bogotá | Suministro de café |
| C010 | Elena Beltrán | B2C, Medellín | Comparación de molinos |
| C011 | Café Horizonte Claro | B2B, Cali | Instalación de equipo |
| C012 | Julián Salcedo | B2C, Bogotá | Solicitud fuera de horario |

## Contactos y resultados

Fechas en hora local de Bogotá, 2026. Cada fila es una interacción ficticia; los identificadores son estables dentro de esta muestra. Los estados indican el resultado narrativo, no una afirmación de que exista una integración real.

El archivo compañero `COMPANY_CO_SERVICE_SCENARIOS.json` contiene los mismos casos en forma estructurada. Sus fechas son desplazamientos relativos al día de provisión para que una demostración nueva aparezca en ventanas recientes; las fechas de la tabla son una ilustración fija y no son el calendario que genera el archivo JSON. Estos doce clientes amplían los perfiles CUS existentes en la ficha principal y no sustituyen su universo comercial.

| ID | Fecha | Cliente | Canal | Caso y conversación resumida | Resultado |
|---|---|---|---|---|---|
| I001 | 2026-10-06 09:10 | C001 | WhatsApp | «Abriremos una cafetería en Chapinero; ¿nos ayudan a planear equipos y espacio?» «Sí, agendemos una asesoría de apertura.» | Cita A001 confirmada |
| I002 | 2026-10-06 11:20 | C002 | Instagram | «¿Qué máquina recomiendan para dos cafés diarios?» «Podemos comparar opciones y presupuesto.» | Orientación; seguimiento pendiente |
| I003 | 2026-10-07 08:40 | C003 | Llamada | «El molino hace un ruido extraño.» «Coordinaremos una revisión técnica.» | Cita A002 confirmada |
| I004 | 2026-10-08 15:00 | C004 | Email | «¿Cuándo llega mi pedido ficticio CC-104?» «Revisamos el despacho y te informamos.» | Resuelto |
| I005 | 2026-10-09 10:15 | C005 | Webchat | «Necesitamos formar a cuatro baristas.» «Tenemos una sesión de capacitación disponible.» | Cita A003 solicitada |
| I006 | 2026-10-12 14:30 | C006 | WhatsApp | «La máquina no calienta. ¿Cómo funciona la garantía?» «Tomaremos los datos del producto y revisaremos el caso.» | Abierto, pendiente de revisión |
| I007 | 2026-10-13 09:05 | C007 | Llamada | «Buscamos diseñar un local pequeño.» «Podemos programar una visita de diagnóstico.» | Cita A004 cancelada por cliente |
| I008 | 2026-10-14 16:25 | C008 | Email | «Quiero devolver el molino sin usar.» «Revisaremos las condiciones de devolución.» | En revisión |
| I009 | 2026-10-20 08:15 | C009 | WhatsApp | «¿Manejan suministro mensual de café?» «Sí; cuéntanos el consumo estimado.» | En seguimiento comercial |
| I010 | 2026-10-22 13:45 | C010 | Facebook | «¿En qué se diferencian estos molinos?» «Uno está pensado para espresso y otro para filtro.» | Resuelto sin cita |
| I011 | 2026-10-27 10:00 | C011 | Llamada | «El equipo llegó; necesitamos instalación.» «Coordinemos una visita técnica.» | Cita A005 confirmada |
| I012 | 2026-11-03 19:40 | C012 | Webchat | «¿Pueden llamarme mañana para asesorarme?» «Recibimos tu solicitud y la revisaremos en horario de atención.» | Pendiente de respuesta humana |
| I013 | 2026-10-17 10:00 | C001 | Email | «¿Podemos revisar la propuesta de equipos?» «La propuesta quedó pendiente de revisión comercial.» | Seguimiento comercial |
| I014 | 2026-10-24 10:00 | C002 | WhatsApp | «Quisiera comparar la máquina recomendada con otra opción.» «Te compartimos las diferencias.» | Resuelto |
| I015 | 2026-10-26 10:00 | C006 | Email | «Adjunté los datos para la garantía.» «Posventa revisará el caso.» | En revisión |
| I016 | 2026-10-29 10:00 | C003 | Llamada | «El molino funciona bien después de la revisión.» «Cerramos el seguimiento.» | Resuelto |
| I017 | 2026-10-31 10:00 | C009 | WhatsApp | «Calculamos veinte kilos mensuales.» «Un asesor revisará una propuesta.» | En seguimiento comercial |
| I018 | 2026-11-02 10:00 | C007 | Llamada | «¿Podemos reprogramar la visita cancelada?» «Registramos una nueva solicitud de diseño.» | Cita A006 solicitada |

## Agenda sintética

| ID | Interacción | Servicio | Inicio local | Estado narrativo |
|---|---|---|---|---|
| A001 | I001 | Asesoría de apertura | 2026-10-08 10:00 | Confirmada, realizada |
| A002 | I003 | Diagnóstico técnico | 2026-10-09 09:00 | Confirmada, realizada |
| A003 | I005 | Capacitación | 2026-10-16 14:00 | Solicitada; no confirmada |
| A004 | I007 | Diseño de espacio | 2026-10-19 10:00 | Cancelada por cliente |
| A005 | I011 | Instalación | 2026-10-30 09:00 | Confirmada; asistencia sin registrar |
| A006 | I018 | Diseño de espacio | Pendiente de acordar | Solicitada; no confirmada |

## Lectura de métricas y límites

En esta muestra hay 18 interacciones, 12 clientes, 5 llamadas, 13 interacciones por canales escritos, 6 solicitudes de agenda y 3 citas confirmadas. Algunos clientes vuelven por otro canal o para hacer seguimiento. Esos conteos describen el archivo, no necesariamente lo que una aplicación ya calcula. Una solicitud no es una cita confirmada; una cita confirmada no prueba asistencia. Las conversaciones anteriores son resúmenes ficticios, no transcripciones íntegras. La muestra no representa volúmenes anuales, tiempos de atención, ventas ni satisfacción.

Para una implementación reproducible, conservar IDs, fechas y relaciones; etiquetar todos los registros como demostración sintética, usar direcciones `example.invalid`, evitar números telefónicos o direcciones reales, no activar conexiones ni enviar comunicaciones y aislar la compañía de los datos reales. Llamadas, duración, resultado, transcripción y vinculación a casos deben mapearse únicamente a un modelo de llamadas real cuando exista; no convertir mensajes en llamadas. Registrar cobertura y lagunas de la aplicación receptora, permisos de acceso y método de actualización/retirada antes de cargar datos.

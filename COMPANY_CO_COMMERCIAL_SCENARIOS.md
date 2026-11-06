# Company Co — escenario comercial y de operaciones

Este escenario amplía `COMPANY_CO_SERVICE_SCENARIOS.json` con datos exclusivamente sintéticos. Su versión estructurada está en `COMPANY_CO_COMMERCIAL_SCENARIOS.json`; no describe clientes, servicios, consumo ni ingresos reales.

Incluye seis oportunidades en distintas etapas para clientes del escenario de atención, [seis documentos de conocimiento](COMPANY_CO_KNOWLEDGE_SCENARIOS.md) sobre apertura, productos, atención y posventa, una asistente de recepción en borrador y tres campañas de correo en borrador: asesorías de apertura, cuidado de equipos y capacitación. Las campañas están vinculadas a conversaciones de ejemplo y no autorizan ni ejecutan envíos. El campo `campaign` del JSON conserva el ejemplo original; `campaigns` contiene el conjunto ampliado.

El ejemplo de consumo muestra 230 mensajes entrantes, 78 respuestas de IA y 12 operaciones de calendario en un ciclo de 30 días. Son cifras de muestra independientes de las 18 interacciones narrativas; no representan una reconstrucción exhaustiva de todos los eventos de ese periodo. Los importes y el consumo son ilustrativos, no son facturas, costos medidos ni cargos reales.

Las aplicaciones consumidoras deben conservar el aislamiento de la compañía sintética, aplicar sus permisos y cifrado habituales, mantener desactivados los efectos externos y no sobrescribir cambios posteriores al repetir la carga. Una selección de rol o un dato sintético no constituye autenticación ni autorización de envío.

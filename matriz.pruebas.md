# Matriz de Pruebas

Este documento registra los casos de prueba realizados sobre la aplicación Flask de gestión de residuos.

---

## Pruebas Smoke (funcionalidad básica)

| ID    | Caso de Prueba        | Input             | Resultado Esperado         | Resultado Actual | Estado |
|-------|-----------------------|-------------------|----------------------------|------------------|--------|
| SMK-01| Carga de Home         | URL raíz (`/`)    | Página carga correctamente | Página carga OK  | OK     |
| SMK-02| Registrar punto válido| Nombre, tipo, ubicación completos | Punto se agrega a la tabla | Punto aparece en tabla | OK |

---

## Pruebas de Caja Negra (validaciones)

| ID    | Caso de Prueba        | Input             | Resultado Esperado         | Resultado Actual | Estado |
|-------|-----------------------|-------------------|----------------------------|------------------|--------|
| BB-01 | Campos vacíos         | Nombre vacío      | Mostrar error / no registrar| No registra      | OK     |
| BB-02 | Tipo de residuo vacío | Tipo vacío        | Mostrar error / no registrar| No registra      | OK     |
| BB-03 | Ubicación vacía       | Ubicación vacía   | Mostrar error / no registrar| No registra      | OK     |
| BB-04 | Límite de caracteres  | Nombre con 500 letras | Sistema corta texto o lanza alerta | Se corta | OK |
| BB-05 | Inyección SQL         | `' OR '1'='1`     | Sistema limpia la entrada y no registra | No registra | OK |
---

## Pruebas de Usabilidad

| ID    | Caso de Prueba        | Input             | Resultado Esperado         | Resultado Actual | Estado |
|-------|-----------------------|-------------------|----------------------------|------------------|--------|
| US-01 | Botón Registrar visible| Página cargada    | Botón verde claramente visible | Visible         | OK     |
| US-02 | Tabla legible         | Puntos registrados| Datos se muestran en columnas | Tabla clara     | OK     |
| US-03 | Estilo responsivo     | Abrir en navegador móvil | Formulario y tabla se adaptan | Se adapta       | OK     |

---

📌 En total: 8 casos de prueba documentados (2 Smoke, 3 Caja Negra, 3 Usabilidad).

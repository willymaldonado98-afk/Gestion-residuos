# Bitácora de Prompts

Este documento registra los prompts utilizados para generar y mejorar la aplicación Flask de gestión de residuos.  
Personales responsables: Willy Maldonado y Matías Fonseca

---

## Prompt 1
Instrucción: Actúa como un desarrollador Fullstack Senior. Crea una app Flask para registrar puntos de reciclaje  
Corrección: Se pidió que agregara validación de campos vacíos  
Resultado: Se generó el archivo app.py con la lógica básica y un formulario en index.html

---

## Prompt 2
Instrucción: Agrega estilo con Bootstrap al formulario  
Corrección: Ajustar diseño para que sea más claro y responsivo  
Resultado: Se aplicaron estilos en index.html usando Bootstrap para mejorar la presentación

---

## Prompt 3
Instrucción: Haz que los puntos registrados se muestren en una tabla  
Corrección: Se pidió que los datos se guardaran en memoria y se listaran en pantalla  
Resultado: Se implementó la tabla en la sección “Puntos registrados” mostrando los datos ingresados

---

## Prompt 4
Instrucción: Agrega validaciones de seguridad (límites de caracteres e inyección SQL)  
Corrección: Se pidió que el sistema rechazara entradas inválidas y limpiara datos peligrosos  
Resultado: Se documentaron pruebas de borde en matriz.pruebas.md para validar seguridad y estabilidad

---

Conclusión: La aplicación se construyó de manera iterativa, mejorando en cada paso con correcciones y pruebas. Se logró un MVP funcional con validaciones básicas, estilo responsivo y pruebas de calidad documentadas.

---
argument-hint: "mensaje del commit"
triggers: ["user", "model"]
allowed-tools: ["exec"]
---

# Objetivo
El propósito de esta habilidad es automatizar el push de cambios al repositorio remoto.

## Paso a paso
1. Ejecuta el comando: git add .
2. Ejecuta el comando: git commit -m "$ARGUMENTS"
3. Ejecuta el comando: git push

## Restricciones
- No modifiques archivos directamente, solo reporta los problemas.

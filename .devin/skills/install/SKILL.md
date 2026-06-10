---
argument-hint: "nombre-del-repositorio o parámetro"
triggers: ["user", "model"]
allowed-tools: ["bash", "read_file", "write_file"]
---

# Objetivo
El propósito de esta habilidad es automatizar la instalacion del CLI.

## Paso a paso
1. Ejecuta el comando: pip install . -e

## Restricciones
- No modifiques archivos directamente, solo reporta los problemas.

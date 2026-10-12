# Comparación de modelos de sentimiento en español

Prototipo académico de clasificación de mensajes de atención al cliente en positivo, neutral y negativo. Se comparan tres modelos públicos de Hugging Face sin ajuste fino.

## Estructura
- `notebooks/`: cuaderno ejecutable en Google Colab.
- `data/`: conjunto sintético de 36 mensajes, CSV y Excel.
- `src/`: validación de datos.
- `results/`: archivos generados al ejecutar el cuaderno.
- `requirements.txt`: dependencias.
- `analisis_comparativo.docx`: informe académico.

## Ejecución
1. Crear repositorio GitHub y subir estos archivos manteniendo las carpetas.
2. Abrir `notebooks/comparacion_sentimiento.ipynb` en Google Colab.
3. Activar GPU T4 desde Entorno de ejecución (si está disponible).
4. Ejecutar celdas en orden; cuando se solicite, subir `data/mensajes.csv`.
5. Para autenticarse opcionalmente, establecer `HF_TOKEN` en los secretos/entorno de Colab; nunca publicar tokens.
6. Descargar `results/metricas.csv`, `results/predicciones.csv` y `results/recomendacion.json` y subirlos al repositorio.

## Datos
36 mensajes sintéticos redactados para la actividad, 12 por clase. No contienen información de clientes reales. No son representativos de producción. Reproducción: archivo CSV incluido y script `src/validar_dataset.py` para validación.

## Conclusiones
No se anticipa un ganador sin ejecutar la evaluación. La selección provisional se automatiza por F1 macro y latencia, y requiere validación con datos reales etiquetados.

## Licencias
Verificar la licencia vigente y condiciones de cada modelo en su ficha de Hugging Face antes de redistribuir pesos o usar comercialmente. El conjunto sintético del proyecto puede reutilizarse con atribución.


## Resultados de ejecución (Tesla T4)

El notebook ejecutado se incluye en `notebooks/`. Las métricas verificadas en su salida se encuentran en `results/metricas.csv` (36 ejemplos sintéticos). F1 macro: RoBERTa 0.9722, DistilBERT 0.4127, BERT 0.7410. Recomendación provisional: RoBERTa. Las cifras no representan validación en producción.

## Publicación

Pendiente: publicar este directorio en una cuenta de GitHub y compartir el enlace del repositorio. No subir tokens ni credenciales.

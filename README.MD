# Sistema Predictivo de Valuación Inmobiliaria para Córdoba Capital

### Proyecto ABP - Álgebra Lineal

---

## Índice

1. [Carátula](#caratula)
2. [Tipo de Proyecto](#tipo-de-proyecto)
3. [Ejes / Unidades Conceptuales](#ejes--unidades-conceptuales)
4. [Problemática / Necesidad / Caso](#problemática--necesidad--caso)
5. [Fundamentación / Hipótesis](#fundamentación--hipótesis)
6. [Objetivo General](#objetivo-general)
7. [Objetivos Específicos](#objetivos-específicos)
8. [Cronograma](#cronograma)
9. [Desarrollo Algebraico y Modelo Matemático](#desarrollo-algebraico-y-modelo-matemático)
10. [Instructivo de Uso del Software](#instructivo-de-uso-del-software)
11. [Poster](#poster)

---

## Carátula

- **Institución:** Instituto Superior Politécnico Córdoba
- **Tecnicatura Superior:** Ciencia de Datos e Inteligencia Artificial
- **Espacio Curricular:** Álgebra

- **Integrantes:**

  - Fátima Muñoz
  - Luis Alberto Lagger
  - Fernando Areosa
  - Guillermo Tissera
  - Thiago Masciotta

- **Cohorte:** 2025
- **Nombre / Título:** _Sistema Predictivo de Valuación Inmobiliaria para Córdoba Capital mediante Regresión Lineal Multivariable_

---

## Tipo de Proyecto

### **Tecnológico**

Este proyecto se desarrolla con un enfoque tecnológico: se implementa un prototipo de software que incorpora métodos de regresión lineal múltiple y álgebra matricial para estimar precios de propiedades.

---

## Ejes / Unidades Conceptuales

- Sistemas de ecuaciones lineales
- Álgebra matricial aplicada
- Regresión lineal múltiple
- Representación de datos y preprocesamiento
- Métricas de evaluación y validación
- Interpretación de coeficientes y significancia

---

## Problemática / Necesidad / Caso

### Problemática identificada

En la práctica del mercado inmobiliario de Córdoba Capital existe la ausencia de una herramienta estandarizada y objetiva que permita estimar el valor de una propiedad a partir de sus características técnicas y contextuales. Esto conlleva:

- Valuaciones subjetivas y discrecionales.
- Sobreprecios y subvaluaciones en transacciones.
- Dificultad para inversores y propietarios para fijar precios justos.
- Falta de transparencia y comparabilidad entre ofertas.

### Caso de uso

Proveer una herramienta web interactiva que, a partir de un conjunto de variables de entrada (metros cuadrados, cantidad de habitaciones, antigüedad, zona, tipo de propiedad, etc.), entregue una estimación de precio basada en un modelo de regresión lineal múltiple entrenado con datos representativos del mercado de Córdoba Capital.

---

## Fundamentación / Hipótesis

### Fundamentación

La regresión lineal múltiple, formulada en términos de álgebra matricial, es un enfoque clásico y sólido para estimar relaciones lineales entre una variable dependiente (precio) y múltiples variables independientes (características de la propiedad). Aplicar este enfoque permite construir un modelo interpretable, reproducible y con fundamentos matemáticos claros, compatible con los objetivos pedagógicos del espacio curricular de Álgebra.

### Hipótesis

Se plantea la hipótesis de trabajo:

> Es posible desarrollar un modelo de regresión lineal múltiple que prediga el valor de propiedades en Córdoba Capital con precisión suficiente para ser útil como herramienta de aproximación (objetivo deseado: R² ≥ 0.85 en datos de validación con un dataset representativo).

### Relevancia profesional y social

- Fomenta la aplicación práctica del álgebra lineal a problemas reales.
- Contribuye a la transparencia del mercado inmobiliario local.
- Provee una herramienta accesible para pequeños inversores y propietarios.

---

## Objetivo General

Desarrollar un sistema de valuación inmobiliaria basado en álgebra lineal que prediga precios de propiedades en Córdoba Capital mediante regresión lineal múltiple, integrando variables clave y proporcionando una interfaz interactiva para su uso.

---

## Objetivos Específicos

1. Recopilar y estructurar un dataset representativo del mercado inmobiliario de Córdoba Capital.
2. Implementar el modelo de regresión lineal múltiple mediante álgebra matricial y técnicas de estimación por mínimos cuadrados.
3. Desarrollar una interfaz web interactiva que permita introducir variables y obtener la predicción de precio.
4. Validar el modelo mediante métricas estadísticas (R², MSE, RMSE, MAE) y técnicas de validación cruzada.
5. Documentar el proceso matemático, de implementación y los resultados obtenidos.

---

## Cronograma

| Momento | Actividad                                | Fechas estimadas |
| ------- | ---------------------------------------- | ---------------- |
| 1       | Elección de grupos y definición del caso | 01/09 - 05/09    |
| 2       | Recopilación y limpieza de datos         | 08/09 - 20/09    |
| 3       | Implementación del modelo                | 21/09 - 03/10    |
| 4       | Desarrollo de la interfaz (Streamlit)    | 04/10 - 09/10    |
| 5       | Validación, pruebas y ajuste             | 10/10 - 12/10    |
| 6       | Entrega final escrita y presentación     | 13/10 - 17/10    |

---

## Desarrollo Algebraico y Modelo Matemático

### 1. Planteo del modelo

Se utiliza una regresión lineal múltiple formulada en términos matriciales:

\[ Y = X\beta + \varepsilon \]

Donde:

- \(Y\) es el vector columna de valores observados (precios).
- \(X\) es la matriz de diseño que incluye una columna de unos para el intercepto y una columna por cada variable predictora.
- \(\beta\) es el vector de coeficientes a estimar.
- \(\varepsilon\) es el vector de errores/residuos.

### 2. Matriz de diseño

Ejemplo de fila de \(X\) (para una observación i):

\[ [1\quad m^2_i\quad hab_i\quad antig_i\quad zona_i\quad tipo_i] \]

Correspondiendo a las variables:

- `m²`: metros cuadrados
- `hab`: cantidad de habitaciones
- `antig`: antigüedad en años
- `zona`: indicador o codificación de zona (variable categórica codificada)
- `tipo`: tipo de propiedad (departamento, casa, PH, etc.)

### 3. Estimación de coeficientes (método de mínimos cuadrados)

La solución de mínimos cuadrados ordinarios (OLS) se calcula mediante la expresión matricial:

\[ \hat{\beta} = (X^{T}X)^{-1} X^{T} Y \]

En implementación práctica se recomienda usar la pseudoinversa o técnicas numéricas estables (por ejemplo `np.linalg.pinv`) para evitar inestabilidades cuando \(X^{T}X\) esté próxima a singular.

### 4. Preprocesamiento y codificación

- Normalización / estandarización de variables numéricas (opcional según técnica).
- Codificación de variables categóricas (one-hot encoding o ordinal encoding según análisis).
- Imputación de valores faltantes cuando corresponda.
- Detección y tratamiento de outliers que puedan sesgar la estimación.

### 5. Métricas de evaluación

- Coeficiente de determinación (R²).
- Error cuadrático medio (MSE).
- Raíz del error cuadrático medio (RMSE).
- Error absoluto medio (MAE).

### 6. Validación

- División entrenamiento/prueba (por ejemplo 80/20).
- Validación cruzada K-fold para estimar la estabilidad del modelo.

---

## Instructivo de Uso del Software

El software desarrollado permite resolver y estimar precios de forma automática e interactiva.

### Tecnologías utilizadas

- **Lenguaje:** Python 3.10+
- **Librerías:** `numpy`, `pandas`, `scikit-learn`, `matplotlib`, `streamlit`
- **Ejecución local o web:** interfaz con Streamlit

---

### Instalación

1. Clonar el repositorio (el enlace en el README es correcto):

```powershell
git clone https://github.com/ferareosa/ABP-Algebra-ISPC-2025.git
cd ABP-Algebra-ISPC-2025
```

2. Crear un entorno virtual e instalar dependencias (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

3. Opcional: en Windows se proporciona un lanzador por lotes (`lanzador.bat`) que ejecuta el script `lanzador.py` para abrir Streamlit automáticamente.

---

### Uso

Hay dos formas recomendadas de ejecutar la interfaz web:

- Ejecutar el lanzador (abre el navegador automáticamente):

```powershell
python lanzador.py
```

- Ejecutar Streamlit directamente (útil para desarrollo):

```powershell
streamlit run interfaz/app_streamlit.py --server.headless true --browser.gatherUsageStats false
```

Al abrirse la aplicación en el navegador podrás:

1. Usar la "Calculadora de Valuación" para ingresar:
   - Metros cuadrados (m²)
   - Número de habitaciones
   - Antigüedad (años)
   - Zona (seleccionable)
   - Tipo de propiedad (seleccionable)
2. Pulsar "Calcular Valuación" para obtener la predicción.
3. Navegar a las pestañas de "Análisis del Modelo", "Dataset y Validación", "Gestión de Datos" e "Información Técnica" para ver métricas, gráficos y administrar la base de datos integrada.

---

### Ejemplo de ejecución (salida de consola)

El proyecto incluye una interfaz de consola y un script de demostración (`main.py`) que producen una salida similar a la siguiente cuando se ejecutan desde la terminal:

```txt
⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️
🏠 SISTEMA DE VALUACIÓN INMOBILIARIA - VERSIÓN DEFINITIVA
⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️

🔬 1. INICIALIZANDO SISTEMA COMPLETO...
   ✅ Base de datos: 150 propiedades registradas

📊 2. ESTADÍSTICAS DEL MERCADO INMOBILIARIO:
   💰 Precio promedio: $123,456 USD
   📏 Metros cuadrados promedio: 95.3 m²

🧠 3. ENTRENANDO MODELO DE REGRESIÓN LINEAL MÚLTIPLE...
   ✅ Modelo entrenado con 5 variables predictoras
   🏆 Precisión del modelo (R²): 0.8794
   📉 Error absoluto medio: $62,213 USD

🔎 5. DEMOSTRACIÓN DE PREDICCIONES EN TIEMPO REAL:

   🏡 EJEMPLO 1 - CASA FAMILIAR:
      • 150m², 3 habitaciones, 8 años, Zona 2 (Céntrica), Casa
      💰 Precio estimado: $234,567 USD
      📐 Precio por m²: $1,563 USD/m²

   🏢 EJEMPLO 2 - DEPARTAMENTO MODERNO:
      • 85m², 2 habitaciones, 3 años, Zona 1 (Centro), Departamento
      💰 Precio estimado: $123,456 USD
      📐 Precio por m²: $1,452 USD/m²

Para abrir la interfaz web en vez de la consola, ejecuta:
    python lanzador.py
o directamente:
    streamlit run interfaz/app_streamlit.py

```

> Nota: los valores numéricos en este ejemplo son ilustrativos. Los números reales dependen del dataset cargado y del entrenamiento del modelo.

---

## Producto Final / Resultados Esperados

| Aspecto                              | Descripción                                                                          |
| ------------------------------------ | ------------------------------------------------------------------------------------ |
| **Producto desarrollado**            | Aplicación Python + interfaz web para estimación de precios inmobiliarios.           |
| **Resultados matemáticos esperados** | Modelo de regresión lineal múltiple implementado y validado con métricas reportadas. |
| **Aplicación didáctica**             | Material de uso pedagógico para entender regresión y álgebra matricial aplicada.     |
| **Impacto social y formativo**       | Facilita acceso a estimaciones objetivas del mercado inmobiliario local.             |

---

### Ecuación final (ejemplo derivado del conjunto de trabajo)

Precio = β₀ + β₁·m² + β₂·habitaciones + β₃·antigüedad + β₄·zona + β₅·tipo

Donde los coeficientes son estimados por la fórmula de mínimos cuadrados.

### Métricas reportadas (ejemplo)

- R² (entrenamiento): 0.8980
- R² (validación): 0.8794
- MAE: $62.213

> Los valores exactos dependen del dataset y del proceso de validación; se incluyen aquí como referencia del proyecto.

---

## Limitaciones y consideraciones

- La regresión lineal asume relaciones lineales entre variables predictoras y la variable objetivo; si existen relaciones no lineales fuertes, pueden requerirse transformaciones o modelos alternativos.
- Calidad y tamaño del dataset afectan fuertemente la capacidad de generalización.
- Variables categóricas mal codificadas o zonas mal definidas pueden introducir sesgos.
- La presencia de outliers puede distorsionar la estimación de coeficientes; es recomendable su detección y tratamiento.

---

## Trabajo futuro / Extensiones posibles

- Incorporar regularización (Ridge, Lasso) para mejorar estabilidad y reducir sobreajuste.
- Explorar modelos no lineales (árboles, random forest, gradient boosting) y comparar desempeño.
- Ampliar el dataset con fuentes públicas y scraping controlado para mejorar representatividad.
- Implementar un API REST simple para exponer el modelo en producción.
- Agregar visualizaciones avanzadas y explicación de modelos (SHAP, LIME) para interpretar predicciones.

---

## Poster

<img src="./ABP-poster.png" alt="poster abp"/>

[Descargar](https://drive.google.com/file/d/1_nYUu0va2f51v84nK2L492AeR_Py_kpb/view?usp=sharing)

---

## Referencias y bibliografía

- Textos básicos de álgebra lineal y estadística aplicada.
- Documentación de `scikit-learn` sobre regresión lineal y métricas.
- Recursos de Streamlit para desarrollo de interfaces interactivas.

---

## Licencia

Este repositorio se entrega con fines académicos. Consultar con el equipo para usos distintos a la evaluación educativa.

---

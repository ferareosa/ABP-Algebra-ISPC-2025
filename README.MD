# Optimización de Recursos para un Microemprendimiento de Comida

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
11. [Producto Final / Resultados Esperados](#producto-final--resultados-esperados)

---

## Carátula

- **Institución:** Instituto Superior Politécnico Córdoba
- **Tecnicatura Superior:** Ciencia de Datos e Inteligencia Artificial
- **Espacio Curricular:** Álgebra

- **Integrantes:**

  > -Fátima Muñoz

  - Luis Alberto Lagger
  - Fernando Areosa
  - Guillermo Tissera
  - Thiago Masciotta

- **Cohorte:** 2025
- **Nombre / Título:** _Optimización de Recursos para un Microemprendimiento de Comida usando Sistemas de Ecuaciones Lineales_

---

## Tipo de Proyecto

### **Tecnológico**

---

## Ejes / Unidades Conceptuales

- Sistemas de ecuaciones lineales
- Representación gráfica de restricciones
- Álgebra matricial aplicada
- Métodos de resolución (Gráfico / Gauss)
- Funciones objetivo y optimización lineal básica

---

## Problemática / Necesidad / Caso

Un estudiante quiere emprender un pequeño negocio de venta de sándwiches y jugos dentro de la facultad.

**Restricciones:**

- Presupuesto disponible: $15.000
- Capacidad máxima de almacenamiento: 50 unidades (sándwiches + jugos)
- Costo unitario sándwich: $300
- Costo unitario jugo: $200
- Precio de venta sándwich: $800
- Precio de venta jugo: $500

**Necesidad:** Maximizar la ganancia respetando las restricciones de presupuesto y capacidad.

---

## Fundamentación / Hipótesis

El proyecto aplica **sistemas de ecuaciones lineales** para resolver un **problema real de optimización** en un contexto accesible para estudiantes.  
Mediante la formulación matemática del problema, se busca obtener la **combinación óptima de producción de sándwiches y jugos** que maximiza la ganancia neta.

**Hipótesis:**

> Si se plantean las restricciones como un sistema de inecuaciones lineales y se utiliza la función objetivo adecuada, es posible determinar la producción óptima de sándwiches y jugos que maximiza la ganancia total.

**Relevancia profesional:**

- Aplicación directa de Álgebra Lineal en problemas reales.
- Comprensión de modelos de optimización.
- Transferencia a contextos emprendedores y productivos reales.

**Impacto:**

- Fomento de habilidades analíticas y de resolución de problemas.
- Potencial de uso como modelo base para otros emprendimientos similares.

---

## Objetivo General

Desarrollar un **modelo matemático y una herramienta de software interactiva** que permita optimizar la producción de sándwiches y jugos maximizando la ganancia bajo restricciones reales de presupuesto y capacidad.

---

## Objetivos Específicos

1. Formular matemáticamente el problema como un sistema de ecuaciones e inecuaciones lineales.
2. Representar gráficamente las restricciones para visualizar el espacio factible.
3. Implementar un modelo algebraico para encontrar la solución óptima.
4. Desarrollar una interfaz simple de uso para introducir parámetros personalizados.
5. Validar la solución mediante métodos manuales y computacionales.

---

## Cronograma

| Momento | Actividad                                | Fechas estimadas |
| ------- | ---------------------------------------- | ---------------- |
| 1       | Elección de grupos y definición del caso | 01/09 - 05/09    |
| 2       | Identificación de la problemática        | 08/09 - 12/09    |
| 3       | Entrega parcial (Evidencia 3)            | 06/10 - 10/10    |
| 4       | Entrega final escrita                    | 13/10 - 17/10    |
| 5       | Defensa oral                             | 20/10 - 24/10    |

---

## Desarrollo Algebraico y Modelo Matemático

### Planteo del Sistema

El problema puede modelarse mediante **ecuaciones lineales con restricciones**:

**Variables:**

- `x`: cantidad de sándwiches a producir
- `y`: cantidad de jugos a producir

**Restricciones:**

1. **Presupuesto total:**

300x + 200y ≤ 15000

2. **Capacidad de almacenamiento:**

x + y ≤ 50

3. **No negatividad:**

x ≥ 0 , y ≥ 0

**Función Objetivo (Ganancia):**

G = 500x + 300y → MAXIMIZAR

---

### Método de Resolución

#### 1. Método Gráfico

1. Representar las restricciones como rectas en el plano.
2. Delimitar la **región factible** (intersección de todas las restricciones).
3. Evaluar la función objetivo `G` en cada **vértice** de dicha región.
4. Escoger el punto `(x, y)` con la **mayor ganancia**.

#### 2. Método Matricial (opcional)

Representación en forma general:

A · X = B

donde  
`A` = matriz de coeficientes,  
`X` = vector de incógnitas `[x, y]`,  
`B` = vector de términos independientes.

Resolución:

X = A⁻¹ · B

o bien mediante **eliminación de Gauss** para verificar consistencia y solución.

---

## Instructivo de Uso del Software

El software desarrollado permite resolver el problema de optimización **de forma automática e interactiva**.

### Tecnologías utilizadas

- **Lenguaje:** Python 3.10+
- **Librerías:** `numpy`, `matplotlib`, `streamlit`
- **Ejecución local o web:** mediante interfaz gráfica con _Streamlit_

---

### Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/ferareosa/ABP-Algebra-ISPC-2025.git
cd optimizacion-sandwiches-jugos
```

2. Crear entorno virtual e instalar dependencias

- Linux / macOS:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

3. Ejecutar la aplicación (Streamlit):

```bash
python -m streamlit run interfaz/app_streamlit.py
```

---

### Uso

1. Ingresar datos personalizados:

   - Costo de sándwich y jugo

   - Precio de venta

   - Presupuesto máximo

   - Capacidad de almacenamiento

2. El sistema calculará automáticamente:

   - Restricciones y región factible

   - Puntos de intersección

   - Ganancia máxima

   - Representación gráfica de la solución

Salida esperada:

```bash
Producción óptima:
x = 30  (sándwiches)
y = 20  (jugos)

Ganancia máxima: $21,000
```

---

### Ejemplo de Ejecución

```txt
    >> Costo sandwich: 300
    >> Costo jugo: 200
    >> Presupuesto total: 15000
    >> Capacidad total: 50

    --> Resultados:
    x = 30, y = 20
    Ganancia total: $21,000
```

Gráficamente, el software mostrará las rectas de restricción y marcará el punto óptimo en el vértice de la región factible.

---

## Producto Final / Resultados Esperados

| Aspecto                              | Descripción                                                                                             |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| **Producto desarrollado**            | Aplicación Python + interfaz web para resolución de problemas de optimización lineal.                   |
| **Resultados matemáticos esperados** | Determinar la combinación óptima `(x, y)` que maximiza la ganancia sin exceder presupuesto o capacidad. |
| **Aplicación didáctica**             | Herramienta educativa para demostrar el uso práctico de álgebra lineal en contextos reales.             |
| **Impacto social y formativo**       | Promueve la comprensión del pensamiento lógico y la capacidad de modelar problemas reales.              |

### Conclusiones

- La aplicación de **sistemas de ecuaciones lineales** permite optimizar decisiones de producción en contextos reales y sencillos.
- El uso de restricciones presupuestarias y de capacidad posibilita **modelar situaciones económicas concretas** y obtener soluciones eficientes.
- El álgebra lineal funciona como **herramienta base para problemas de optimización**, brindando claridad matemática y soporte a la toma de decisiones.
- El software desarrollado no solo resuelve el problema automáticamente, sino que también sirve como **material pedagógico** para comprender el proceso paso a paso.
- Este proyecto integra **modelado matemático + programación + aplicación práctica**, demostrando la potencia del enfoque ABP (Aprendizaje Basado en Proyectos) en la formación técnica y científica.

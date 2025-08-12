## Car Insights – Análisis de Vehículos Usados

Esta es una aplicación web interactiva construida con Streamlit, Pandas y Plotly Express que permite explorar un conjunto de datos de anuncios de vehículos usados.

Funcionalidad
	•	Visualización de histogramas: El usuario puede activar una casilla para generar un histograma interactivo del kilometraje (odometer) de los vehículos.
	•	Gráfico de dispersión: Otra casilla permite generar un diagrama de dispersión mostrando la relación entre el kilometraje (odometer) y el precio (price), coloreado según la condición del vehículo (condition).
	•	Datos cargados dinámicamente desde un archivo CSV [`vehicles_us.csv`](https://github.com/Misaelfc/cars-insights/blob/main/vehicles_us.csv).

Uso
	1.	Asegúrate de tener instaladas las dependencias del archivo requirements.txt:
    pip install -r requirements.txt

	2.	Ejecuta la aplicación:
    streamlit run app.py

	3.	Abre el enlace que aparece en la terminal para acceder a la aplicación web en tu navegador.

Estructura del proyecto
.
├── README.md

├── app.py

├── vehicles_us.csv

├── requirements.txt

└── notebooks
	└── EDA.ipynb

# UniMatch – Recomendaciones Inteligentes para tu Vida Universitaria

UniMatch es un sistema de recomendaciones diseñado para estudiantes universitarios, con el objetivo de sugerir actividades extracurriculares personalizadas basadas en sus intereses, ubicación y disponibilidad de tiempo. Utiliza una base de datos de grafos (Neo4j) para modelar las relaciones entre usuarios, actividades y categorías de interés.

## Tecnologías Utilizadas

- **Frontend:** React + Vite
- **Backend:** Flask (Python)
- **Base de Datos:** Neo4j (modelo orientado a grafos)
- **Lenguaje de consulta:** Cypher

## Objetivo del Proyecto

El sistema permitirá:
- Registrar estudiantes y actividades extracurriculares.
- Relacionar estudiantes con categorías de interés.
- Recomendar actividades usando algoritmos sobre grafos.
- Mostrar las recomendaciones en una interfaz web simple y clara.

## Estructura del Proyecto

```
/unimatch/
│
├── backend/              # API Flask para gestionar usuarios y actividades
│   ├── app.py
│   ├── routes/
│   └── services/
│
├── frontend/             # Interfaz React con Vite
│   ├── src/
│   └── vite.config.js
│
├── neo4j/                # Scripts para inicializar y poblar la base de datos
│   ├── schema.cql
│   └── example_data.cql
│
├── README.md
└── requirements.txt
```

## Diseno Preeliminar de la Base de Datos

![BD Design](https://raw.githubusercontent.com/Julio-orellana/Proyecto-2-DSA/main/docs/design/bd_inicial.png)

## Comunicacion Actual entre backend y frontend

![Comunicacion Example](https://raw.githubusercontent.com/Julio-orellana/Proyecto-2-DSA/main/docs/design/ProjectArchitecture.png)

## Funcionalidades Principales (Fase 1)

- Definición del modelo de datos en grafos (usuarios, actividades, categorías).
- Pseudocódigo del algoritmo de recomendación.
- Prototipo inicial del frontend.
- Conexión básica entre Flask y Neo4j.

## Cómo Ejecutar el Proyecto (preliminar)

### Requisitos
- Python 3.10+
- Node.js 18+
- Neo4j Desktop o Aura
- pipenv o virtualenv

### Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Base de Datos
- Ejecuta `schema.cql` y `example_data.cql` en Neo4j Browser.

## Contribuyentes

- Diego Guevara  
- Julio Orellana 24207 
- Juan Jose Rivas

## Licencia

Este proyecto es parte del curso de Algoritmos y Estructura de Datos – Universidad del Valle de Guatemala.

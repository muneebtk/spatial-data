# Spatial Data Management API

A Django-based API for storing, updating, and retrieving spatial data, specifically for point and polygon geometries. This API leverages Django Rest Framework (DRF) and GeoDjango to handle spatial data efficiently.

---

## **Features**

### **1. Point Data Management**
- **Add Points**: Store geographical points with metadata.
- **Update Points**: Modify existing point data.
- **Retrieve Points**: Fetch point data within a specified area or based on filters.

### **2. Polygon Data Management**
- **Add Polygons**: Store geographical polygons with metadata.
- **Update Polygons**: Modify existing polygon data.
- **Retrieve Polygons**: Fetch polygons intersecting or within a specified area.

---

## **Setup Instructions**

### **Prerequisites**
1. Python 3.10+
2. PostgreSQL with PostGIS extension
3. Pipenv or Virtualenv (recommended for virtual environments)

### **Installation**

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database settings in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.contrib.gis.db.backends.postgis',
           'NAME': '<database_name>',
           'USER': '<username>',
           'PASSWORD': '<password>',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. Apply the migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## **API Endpoints**

### **Point Data Endpoints**

| Method | Endpoint            | Description                |
|--------|---------------------|----------------------------|
| POST   | `/api/points/`      | Create a new point record  |
| GET    | `/api/points/`      | List all point records     |
| GET    | `/api/points/<id>/` | Retrieve a specific point  |
| PUT    | `/api/points/<id>/` | Update a specific point    |
| DELETE | `/api/points/<id>/` | Delete a specific point    |

### **Polygon Data Endpoints**

| Method | Endpoint              | Description                  |
|--------|-----------------------|------------------------------|
| POST   | `/api/polygons/`      | Create a new polygon record  |
| GET    | `/api/polygons/`      | List all polygon records     |
| GET    | `/api/polygons/<id>/` | Retrieve a specific polygon  |
| PUT    | `/api/polygons/<id>/` | Update a specific polygon    |
| DELETE | `/api/polygons/<id>/` | Delete a specific polygon    |

---

## **Testing**

This project uses `pytest` for testing.

### **Run Tests**
```bash
pytest
```

---

## **Technology Stack**
- **Backend**: Django, Django Rest Framework (DRF), GeoDjango
- **Database**: PostgreSQL with PostGIS
- **Testing**: Pytest

---


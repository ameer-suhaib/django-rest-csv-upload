# CSV Upload API with Django and DRF

## Overview
This project is a Django REST API that allows users to upload a CSV file containing user data (name, email, age). The API validates and stores the data in the database while returning a summary of the processed records.

## Features
- Upload CSV files via a `POST` request.
- Validate CSV content and store valid records in the database.
- Return a response with details of saved and rejected records.
- Basic API testing endpoint.

---

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/csv-upload-api.git
cd myproject
```

### 2. Create & Activate a Virtual Environment
```sh
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Apply Migrations
```sh
python manage.py migrate
```

### 5. Run the Server
```sh
python manage.py runserver
```
The server will start at:  
📌 **http://127.0.0.1:8000/**

---

## API Endpoints

### 1. Test API Endpoint
#### **Endpoint:**
```http
GET /test/
```
#### **Response:**
```json
{
  "message": "Hello World!"
}
```

### 2. Upload CSV File
#### **Endpoint:**
```http
POST /upload/
```
#### **Request:**
- **Headers:** `Content-Type: multipart/form-data`
- **Body:** Upload a `.csv` file with columns: `name,email,age`

#### **Example Request (cURL):**
```sh
curl -X POST http://127.0.0.1:8000/myapp/upload/ \
    -F "file=@users.csv"
```

#### **Example Response:**
```json
{
  "total_saved": 10,
  "total_rejected": 2,
  "validation_errors": [
    {"email": "invalid@example.com", "errors": {"email": ["Enter a valid email."]}}
  ]
}
```


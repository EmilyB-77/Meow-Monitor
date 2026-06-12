# Meow Monitor - API Documentation

## Overview

Meow Monitor provides a RESTful API for managing cat health, feeding schedules, and mood tracking. The API is built with FastAPI and uses JWT for authentication.

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

All endpoints (except auth) require a JWT token in the Authorization header:

```
Authorization: Bearer <your_access_token>
```

## Endpoints

### Authentication

#### Register User
```http
POST /users/register
Content-Type: application/json

{
  "username": "string",
  "email": "user@example.com",
  "password": "string",
  "full_name": "string"
}
```

#### Login
```http
POST /users/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "string"
}

Response:
{
  "access_token": "string",
  "refresh_token": "string",
  "token_type": "bearer"
}
```

#### Get Current User
```http
GET /users/me
Authorization: Bearer <token>

Response:
{
  "id": "uuid",
  "username": "string",
  "email": "user@example.com",
  "full_name": "string",
  "is_active": true,
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

### Cats

#### List Cats
```http
GET /cats?skip=0&limit=100
Authorization: Bearer <token>

Response: Array of cat objects
```

#### Create Cat
```http
POST /cats
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "Whiskers",
  "breed": "Persian",
  "date_of_birth": "2020-01-01T00:00:00Z",
  "color": "Orange",
  "weight_kg": 4.5,
  "microchip_number": "123456789",
  "description": "A friendly orange tabby"
}
```

#### Get Cat
```http
GET /cats/{cat_id}
Authorization: Bearer <token>
```

#### Update Cat
```http
PUT /cats/{cat_id}
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "Updated Name",
  "weight_kg": 5.0
}
```

#### Delete Cat
```http
DELETE /cats/{cat_id}
Authorization: Bearer <token>
```

### Health Records

#### List Health Records
```http
GET /cats/{cat_id}/health?skip=0&limit=100
Authorization: Bearer <token>
```

#### Create Health Record
```http
POST /cats/{cat_id}/health
Authorization: Bearer <token>
Content-Type: application/json

{
  "record_type": "vaccination",
  "title": "Annual Vaccination",
  "description": "Annual checkup and vaccination",
  "veterinarian": "Dr. Smith",
  "clinic_name": "Happy Paws Clinic",
  "notes": "Cat is healthy",
  "cost": "100.00",
  "recorded_date": "2024-01-01T00:00:00Z",
  "next_due_date": "2025-01-01T00:00:00Z"
}
```

#### Get Health Record
```http
GET /cats/{cat_id}/health/{record_id}
Authorization: Bearer <token>
```

#### Update Health Record
```http
PUT /cats/{cat_id}/health/{record_id}
Authorization: Bearer <token>
Content-Type: application/json

{
  "notes": "Updated notes",
  "is_completed": true
}
```

#### Delete Health Record
```http
DELETE /cats/{cat_id}/health/{record_id}
Authorization: Bearer <token>
```

### Feeding

#### List Feeding Logs
```http
GET /cats/{cat_id}/feeding/logs?skip=0&limit=100
Authorization: Bearer <token>
```

#### Create Feeding Log
```http
POST /cats/{cat_id}/feeding/logs
Authorization: Bearer <token>
Content-Type: application/json

{
  "food_type": "wet",
  "portion_grams": 100,
  "meal_name": "Breakfast",
  "notes": "Cat ate all food",
  "fed_at": "2024-01-01T08:00:00Z"
}
```

#### List Feeding Schedules
```http
GET /cats/{cat_id}/feeding/schedules
Authorization: Bearer <token>
```

#### Create Feeding Schedule
```http
POST /cats/{cat_id}/feeding/schedules
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "Daily Breakfast",
  "food_type": "dry",
  "portion_grams": 50,
  "time_of_day": "08:00:00",
  "days_of_week": "1111111",
  "notes": "Morning meal"
}
```

### Mood Tracking

#### List Mood Logs
```http
GET /cats/{cat_id}/mood?skip=0&limit=100
Authorization: Bearer <token>
```

#### Create Mood Log
```http
POST /cats/{cat_id}/mood
Authorization: Bearer <token>
Content-Type: application/json

{
  "mood": "happy",
  "energy_level": 8,
  "appetite_level": 9,
  "sleep_quality": 7,
  "activities": "playing, sleeping",
  "notes": "Very active today",
  "recorded_at": "2024-01-01T14:00:00Z"
}
```

#### Get Mood Analysis
```http
GET /cats/{cat_id}/mood/analysis/summary?days=30
Authorization: Bearer <token>

Response:
{
  "average_mood": "happy",
  "average_energy": 7.5,
  "average_appetite": 8.2,
  "total_logs": 30
}
```

## Error Responses

All errors follow this format:

```json
{
  "detail": "Error message"
}
```

Common HTTP status codes:
- `200`: Success
- `201`: Created
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `422`: Unprocessable Entity (validation error)
- `500`: Internal Server Error

## Interactive API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

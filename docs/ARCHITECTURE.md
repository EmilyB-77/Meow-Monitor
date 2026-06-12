# Meow Monitor - Architecture

## Overview

Meow Monitor follows a clean architecture pattern with clear separation of concerns and modular design principles.

## Architecture Layers

### 1. **Presentation Layer** (Frontend)
- React components with TypeScript
- Redux for state management
- Tailwind CSS for styling
- API service layer for HTTP requests

### 2. **API Layer** (Backend - FastAPI)
- RESTful endpoints organized by resource
- Request validation with Pydantic
- JWT authentication and authorization
- CORS middleware for frontend communication

### 3. **Business Logic Layer** (Services)
- Business rules and workflows
- Data validation and transformation
- Cross-cutting concerns (logging, error handling)

### 4. **Data Access Layer** (Repository Pattern)
- SQLAlchemy ORM for database operations
- Async database sessions
- Query builders and repositories

### 5. **Database Layer** (PostgreSQL)
- Relational data model
- UUID primary keys
- Soft deletes and audit trails

## Project Structure

```
meow-monitor/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── endpoints/      # Route handlers
│   │   │   │   │   ├── cats.py
│   │   │   │   │   ├── health.py
│   │   │   │   │   ├── feeding.py
│   │   │   │   │   ├── mood.py
│   │   │   │   │   └── users.py
│   │   │   │   └── dependencies.py  # Dependency injection
│   │   │   └── dependencies.py
│   │   ├── core/
│   │   │   ├── config.py            # Settings
│   │   │   ├── security.py          # JWT, password hashing
│   │   │   └── constants.py         # App constants
│   │   ├── db/
│   │   │   ├── database.py          # DB connection
│   │   │   ├── init.sql             # DB initialization
│   │   │   └── migrations/          # Alembic migrations
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── cat.py
│   │   │   ├── health.py
│   │   │   ├── feeding.py
│   │   │   └── mood.py
│   │   ├── schemas/                 # Pydantic schemas
│   │   │   ├── user.py
│   │   │   ├── cat.py
│   │   │   ├── health.py
│   │   │   ├── feeding.py
│   │   │   └── mood.py
│   │   ├── services/                # Business logic (TODO)
│   │   │   ├── cat_service.py
│   │   │   ├── health_service.py
│   │   │   ├── feeding_service.py
│   │   │   └── mood_service.py
│   │   └── main.py                  # FastAPI app
│   ├── tests/
│   │   ├── conftest.py              # Pytest fixtures
│   │   ├── test_api/
│   │   │   ├── test_health.py
│   │   │   ├── test_cats.py
│   │   │   └── ...
│   │   └── test_services/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── components/              # Reusable components
│   │   │   ├── Header.tsx
│   │   │   ├── CatCard.tsx
│   │   │   └── ...
│   │   ├── pages/                   # Page components
│   │   │   ├── Dashboard.tsx
│   │   │   ├── CatsList.tsx
│   │   │   └── ...
│   │   ├── redux/                   # State management
│   │   │   ├── store.ts
│   │   │   └── slices/
│   │   │       ├── authSlice.ts
│   │   │       ├── catsSlice.ts
│   │   │       └── ...
│   │   ├── services/                # API services
│   │   │   └── api.ts
│   │   ├── types/                   # TypeScript types
│   │   │   ├── cat.ts
│   │   │   ├── health.ts
│   │   │   └── ...
│   │   ├── App.tsx
│   │   ├── App.css
│   │   └── index.tsx
│   ├── public/
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   ├── Dockerfile
│   └── .env.example
├── docker-compose.yml
├── .github/
│   └── workflows/
│       ├── backend-tests.yml
│       ├── frontend-tests.yml
│       └── lint.yml
└── docs/
    ├── SETUP.md
    ├── API.md
    └── ARCHITECTURE.md
```

## Data Models

### User
- `id` (UUID, Primary Key)
- `email` (String, Unique)
- `username` (String, Unique)
- `hashed_password` (String)
- `full_name` (String, Optional)
- `is_active` (Boolean)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### Cat
- `id` (UUID, Primary Key)
- `owner_id` (UUID, Foreign Key → User)
- `name` (String)
- `breed` (String, Optional)
- `date_of_birth` (DateTime, Optional)
- `color` (String, Optional)
- `weight_kg` (Float, Optional)
- `microchip_number` (String, Unique, Optional)
- `description` (String, Optional)
- `profile_picture_url` (String, Optional)
- `is_active` (Boolean)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### HealthRecord
- `id` (UUID, Primary Key)
- `cat_id` (UUID, Foreign Key → Cat)
- `record_type` (String) - vaccination, checkup, medication, surgery, dental, etc.
- `title` (String)
- `description` (Text, Optional)
- `veterinarian` (String, Optional)
- `clinic_name` (String, Optional)
- `notes` (Text, Optional)
- `cost` (String, Optional)
- `recorded_date` (DateTime)
- `next_due_date` (DateTime, Optional)
- `is_completed` (Boolean)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### FeedingLog
- `id` (UUID, Primary Key)
- `cat_id` (UUID, Foreign Key → Cat)
- `food_type` (String) - wet, dry, mixed
- `portion_grams` (Float)
- `meal_name` (String, Optional)
- `notes` (String, Optional)
- `fed_at` (DateTime)
- `created_at` (DateTime)

### FeedingSchedule
- `id` (UUID, Primary Key)
- `cat_id` (UUID, Foreign Key → Cat)
- `name` (String)
- `food_type` (String) - wet, dry, mixed
- `portion_grams` (Float)
- `time_of_day` (Time)
- `days_of_week` (String) - "1111111" for daily, "1010101" for weekdays
- `is_active` (Boolean)
- `notes` (String, Optional)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### MoodLog
- `id` (UUID, Primary Key)
- `cat_id` (UUID, Foreign Key → Cat)
- `mood` (String) - happy, content, neutral, anxious, grumpy, playful, tired
- `energy_level` (Integer, 1-10)
- `appetite_level` (Integer, 1-10)
- `sleep_quality` (Integer, 1-10, Optional)
- `activities` (Text, Optional)
- `notes` (Text, Optional)
- `recorded_at` (DateTime)
- `created_at` (DateTime)
- `updated_at` (DateTime)

## Design Patterns Used

### Repository Pattern
- Abstracts data access logic
- Makes code testable and maintainable
- Easy to switch database implementations

### Service Layer Pattern
- Encapsulates business logic
- Separates concerns between endpoints and business logic
- Enables code reuse across endpoints

### Dependency Injection
- FastAPI's `Depends()` for injecting dependencies
- Redux selectors in frontend
- Makes testing easier with mock dependencies

### Factory Pattern
- Database session factory
- Redux store configuration
- API client factory

## Security Measures

1. **Authentication**: JWT tokens with expiration
2. **Authorization**: Role-based access control (RBAC)
3. **Password Security**: Bcrypt hashing
4. **Input Validation**: Pydantic schemas
5. **CORS**: Configured for frontend origin
6. **SQL Injection**: Protected by SQLAlchemy ORM
7. **Secrets Management**: Environment variables

## Performance Optimizations

1. **Async/Await**: Non-blocking database operations
2. **Connection Pooling**: SQLAlchemy connection pool
3. **Caching**: Redis integration (optional)
4. **Pagination**: Limit/offset queries
5. **Indexes**: Database indexes on frequently queried fields
6. **Code Splitting**: Frontend lazy loading

## Testing Strategy

### Backend
- **Unit Tests**: Services and utilities
- **Integration Tests**: API endpoints with test database
- **E2E Tests**: Full workflows
- **Coverage Target**: 80%+

### Frontend
- **Unit Tests**: Component and utility tests
- **Integration Tests**: Redux store interactions
- **E2E Tests**: User workflows (Cypress/Playwright)

## CI/CD Pipeline

1. **Code Push**: Triggered on push/PR
2. **Backend Tests**: Python tests + coverage
3. **Frontend Tests**: Jest tests + coverage
4. **Linting**: Black, flake8, ESLint, Prettier
5. **Security Scan**: Bandit, Safety
6. **Build**: Docker images (optional)
7. **Deploy**: To staging/production (optional)

## Future Enhancements

1. **Real-time Updates**: WebSocket integration
2. **Image Upload**: S3/Cloud storage
3. **Notifications**: Push notifications for reminders
4. **Mobile App**: React Native version
5. **Analytics**: Mood/health trend analysis
6. **Social Features**: Share cat profiles
7. **Multi-user**: Vet access, family sharing

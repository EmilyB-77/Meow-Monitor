# Meow Monitor 🐱

A comprehensive full-stack web application for tracking your cats' health, feeding schedules, and mood patterns.

## Overview

Meow Monitor is a professional-grade application designed for cat owners who want to maintain detailed records of their feline companions' wellbeing. Built with modern technologies and architectural best practices, it demonstrates full-stack development expertise.

## Features

### Core Functionality
- **Multi-Cat Management**: Track multiple cats with individual profiles
- **Health Tracking**: Log medical events, vaccinations, and health metrics
- **Feeding Schedule**: Manage and monitor feeding times and portions
- **Mood Tracking**: Record and analyze your cats' behavioral patterns
- **Photo Gallery**: Upload and organize cat photos with timestamps
- **Dashboard**: Real-time overview of all cats' status

### Technical Highlights
- RESTful API with async operations
- Real-time WebSocket updates
- User authentication and authorization
- Responsive React frontend with TypeScript
- PostgreSQL database with migrations
- Docker containerization
- CI/CD pipeline with GitHub Actions
- Comprehensive test coverage
- Professional error handling and logging

## Tech Stack

### Backend
- **Framework**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL 15+
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Task Queue**: Celery (optional, for background jobs)

### Frontend
- **Library**: React 18+
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State Management**: Redux Toolkit
- **HTTP Client**: Axios

### DevOps
- **Containerization**: Docker & Docker Compose
- **CI/CD**: GitHub Actions
- **Code Quality**: Black, flake8, ESLint, Prettier
- **Testing**: pytest, Jest

## Project Structure

```
meow-monitor/
├── backend/                 # FastAPI application
│   ├── app/
│   │   ├── api/           # API endpoints
│   │   ├── models/        # SQLAlchemy models
│   │   ├── schemas/       # Pydantic schemas
│   │   ├── core/          # Configuration & security
│   │   ├── db/            # Database setup
│   │   └── main.py        # FastAPI app
│   ├── tests/             # Unit & integration tests
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/              # React application
│   ├── src/
│   │   ├── components/    # Reusable components
│   │   ├── pages/         # Page components
│   │   ├── redux/         # Redux store
│   │   ├── services/      # API services
│   │   └── App.tsx
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml     # Multi-container setup
├── .github/workflows/     # GitHub Actions CI/CD
└── docs/                  # Documentation
    ├── SETUP.md
    ├── API.md
    └── ARCHITECTURE.md
```

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Git

### Local Development

1. **Clone and setup**
   ```bash
   git clone https://github.com/EmilyB-77/meow-monitor.git
   cd meow-monitor
   ```

2. **Start services**
   ```bash
   docker-compose up -d
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

4. **Run tests**
   ```bash
   # Backend
   docker-compose exec backend pytest

   # Frontend
   docker-compose exec frontend npm test
   ```

## API Endpoints

### Cats
- `GET /api/v1/cats` - List all cats
- `POST /api/v1/cats` - Create a new cat
- `GET /api/v1/cats/{cat_id}` - Get cat details
- `PUT /api/v1/cats/{cat_id}` - Update cat
- `DELETE /api/v1/cats/{cat_id}` - Delete cat

### Health
- `GET /api/v1/cats/{cat_id}/health` - Get health records
- `POST /api/v1/cats/{cat_id}/health` - Add health record
- `GET /api/v1/cats/{cat_id}/health/{record_id}` - Get health record details

### Feeding
- `GET /api/v1/cats/{cat_id}/feeding/logs` - Get feeding logs
- `POST /api/v1/cats/{cat_id}/feeding/logs` - Log feeding
- `GET /api/v1/cats/{cat_id}/feeding/schedules` - Get feeding schedule

### Mood
- `GET /api/v1/cats/{cat_id}/mood` - Get mood logs
- `POST /api/v1/cats/{cat_id}/mood` - Log mood
- `GET /api/v1/cats/{cat_id}/mood/analysis/summary` - Get mood analysis

## Architecture

### Clean Architecture
The project follows clean architecture principles with clear separation of concerns:
- **Entities**: Core business objects
- **Use Cases**: Business logic and workflows
- **Interface Adapters**: Controllers, presenters, repositories
- **Frameworks**: FastAPI, React, PostgreSQL

### Design Patterns
- Repository Pattern for data access
- Service Layer for business logic
- Dependency Injection for modularity
- Factory Pattern for object creation

## Testing

### Backend
- Unit tests for services and utilities
- Integration tests for API endpoints
- Database fixtures and mocking
- Coverage target: 80%+

### Frontend
- Component testing with React Testing Library
- Redux store testing
- API integration mocking

## CI/CD

GitHub Actions workflows automate:
- Code linting and formatting checks
- Unit and integration tests
- Build verification
- Deployment (optional)

## Development Workflow

1. Create feature branch: `git checkout -b feature/your-feature`
2. Make changes and commit: `git commit -am 'Add feature'`
3. Push to branch: `git push origin feature/your-feature`
4. Open Pull Request

All PRs must pass tests and code quality checks before merging.

## Production Deployment

The application is containerized and ready for deployment to:
- Docker Hub / Container registries
- Kubernetes clusters
- Cloud platforms (AWS ECS, Google Cloud Run, Azure Container Instances, etc.)

See [docs/SETUP.md](./docs/SETUP.md) for deployment instructions.

## Code Quality

```bash
# Format code
docker-compose exec backend black .
docker-compose exec frontend npm run format

# Lint
docker-compose exec backend flake8
docker-compose exec frontend npm run lint
```

## Contributing

1. Follow PEP 8 (Python) and ESLint (JavaScript) standards
2. Write tests for new features
3. Update documentation
4. Ensure all tests pass before submitting PR

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines.

## License

MIT License - See LICENSE file for details

## Author

Emily B. - Full Stack Software Engineer

---

**Built to showcase professional full-stack development practices** 🚀

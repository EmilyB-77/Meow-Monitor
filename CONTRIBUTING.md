# Contributing to Meow Monitor

## Code of Conduct

This project is committed to providing a welcoming and inclusive environment for all contributors.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/meow-monitor.git`
3. Create a feature branch: `git checkout -b feature/your-feature-name`
4. Set up development environment (see docs/SETUP.md)

## Development Workflow

1. **Create a branch** for each feature or bug fix
2. **Write tests** for new functionality
3. **Follow code style** guidelines (see below)
4. **Commit frequently** with clear messages
5. **Push to your fork** and create a Pull Request

## Code Style Guidelines

### Python (Backend)

- Follow PEP 8 style guide
- Use Black for code formatting
- Use isort for import sorting
- Type hints are required
- Docstrings for all public functions/classes

```python
def create_cat(cat_data: CatCreate) -> Cat:
    """Create a new cat record.
    
    Args:
        cat_data: Cat creation schema
        
    Returns:
        Created cat object
    """
    # Implementation
```

### TypeScript/JavaScript (Frontend)

- Follow ESLint configuration
- Use Prettier for formatting
- Type all React props and functions
- Functional components with hooks
- Clear component naming

```typescript
interface CatCardProps {
  cat: Cat;
  onUpdate: (cat: Cat) => void;
}

const CatCard: React.FC<CatCardProps> = ({ cat, onUpdate }) => {
  // Implementation
};
```

## Testing Requirements

### Backend
- Minimum 80% code coverage
- Unit tests for services
- Integration tests for API endpoints
- Fixtures for common test data

```python
@pytest.mark.asyncio
async def test_create_cat(client, test_db):
    """Test creating a cat."""
    response = await client.post("/api/v1/cats", json=cat_data)
    assert response.status_code == 201
```

### Frontend
- Test user interactions
- Mock API responses
- Redux state changes

```typescript
test('renders cat name', () => {
  render(<CatCard cat={mockCat} onUpdate={jest.fn()} />);
  expect(screen.getByText(mockCat.name)).toBeInTheDocument();
});
```

## Commit Message Format

Follow conventional commit format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Test additions/changes
- `chore`: Build, dependencies, etc.

Example:
```
feat(feeding): add meal time predictions

Implement machine learning model to predict optimal feeding times
based on historical mood and energy patterns.

Fixes #123
```

## Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new features
3. **Update CHANGELOG** (if maintained)
4. **Ensure all checks pass** (tests, linting, coverage)
5. **Request review** from maintainers
6. **Address review comments** promptly
7. **Squash commits** if requested

## Documentation

- Update README.md for user-facing changes
- Update docs/API.md for endpoint changes
- Add docstrings for all public APIs
- Include usage examples

## Issue Reporting

When reporting issues, include:

1. **Description**: Clear description of the issue
2. **Steps to Reproduce**: Exact steps to reproduce
3. **Expected vs Actual**: What should happen vs what happens
4. **Environment**: OS, Python/Node version, etc.
5. **Screenshots/Logs**: If applicable

## Feature Requests

For feature requests, please:

1. Check existing issues/discussions
2. Provide detailed description
3. Explain use case and benefits
4. Provide examples or mockups if applicable

## Code Review

Reviewers look for:

- ✅ Code follows style guidelines
- ✅ Tests are included and pass
- ✅ Documentation is updated
- ✅ No performance regressions
- ✅ Security considerations
- ✅ Clear commit messages

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

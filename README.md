# Procurement & Inventory Management System

A cost-effective, open-source-based procurement, inventory, and Amazon sales data integration system.

## Features

- 🌐 Live sync with Amazon SP-API
- 📄 CSV-based fallback/import workflows
- 🧱 Modular, scalable architecture
- 🔄 Real-time inventory management
- 📊 Multi-channel sales integration
- 📈 Analytics and reporting

## System Architecture

The system consists of several key components:

1. **Open-Source ERP Integration**
   - Purchase order management
   - Supplier management
   - Inventory tracking
   - Multi-currency support

2. **Amazon SP-API Integration**
   - Real-time product sync
   - Inventory management
   - Order processing
   - Fulfillment status updates

3. **CSV Import System**
   - Automated file processing
   - Data validation
   - Error handling
   - Manual upload interface

4. **Middleware/API Layer**
   - RESTful API endpoints
   - Authentication/Authorization
   - Data transformation
   - Logging and monitoring

## Prerequisites

- Python 3.9+
- PostgreSQL 13+
- Redis (for task queue)
- Docker (optional)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd procurement-system
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. Initialize the database:
   ```bash
   python scripts/init_db.py
   ```

## Configuration

Create a `.env` file with the following variables:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/procurement_db

# Amazon SP-API
AMAZON_REFRESH_TOKEN=your_refresh_token
AMAZON_CLIENT_ID=your_client_id
AMAZON_CLIENT_SECRET=your_client_secret

# Redis
REDIS_URL=redis://localhost:6379/0

# API Settings
API_SECRET_KEY=your_secret_key
API_ALGORITHM=HS256
```

## Running the Application

1. Start the API server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Start the Celery worker:
   ```bash
   celery -A app.worker worker --loglevel=info
   ```

3. Start the CSV import listener:
   ```bash
   python scripts/csv_listener.py
   ```

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Development

### Code Style

This project uses:
- Black for code formatting
- isort for import sorting
- flake8 for linting

Run the formatters:
```bash
black .
isort .
flake8
```

### Testing

Run tests with pytest:
```bash
pytest
```

## License

MIT License

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 
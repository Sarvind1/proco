# Procurement System API

A comprehensive FastAPI-based procurement and inventory management system with integrated Amazon Selling Partner API support. Manage products, suppliers, purchase orders, and synchronize inventory with Amazon seamlessly.

## Features

- **Product Management** - Create, update, and manage product catalog with SKUs and ASIN tracking
- **Inventory Management** - Track inventory movements, stock levels, and reorder thresholds
- **Purchase Order System** - Create and manage POs with supplier tracking
- **Amazon Integration** - Sync inventory and orders with Amazon Selling Partner API
- **CSV Import** - Bulk import products, inventory, and purchase orders from CSV files
- **User Authentication** - JWT-based authentication with role-based access control
- **Async Task Processing** - Background job execution using Celery for syncing and imports
- **RESTful API** - Complete REST API with interactive Swagger documentation

## Tech Stack

- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: SQLite (development) / PostgreSQL (production-ready)
- **Task Queue**: Celery
- **Data Processing**: pandas
- **Authentication**: JWT + bcrypt
- **API Integration**: Amazon Selling Partner API

## Setup

### Prerequisites
- Python 3.8+
- pip / venv
- Redis (for Celery task queue, optional for development)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd procurement-api
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Initialize database:
```bash
python scripts/init_db.py
python scripts/seed_data.py
```

6. Run the application:
```bash
uvicorn app.main:app --reload
```

API documentation available at: `http://localhost:8000/docs`

## Usage

### Example API Calls

**Create a Product:**
```bash
curl -X POST http://localhost:8000/api/v1/products \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "sku": "PROD001",
    "name": "Sample Product",
    "price": 99.99,
    "quantity": 100
  }'
```

**Import Products from CSV:**
```bash
curl -X POST http://localhost:8000/api/v1/tasks/import-products \
  -H "Authorization: Bearer <token>" \
  -F "file=@products.csv"
```

**Sync Inventory with Amazon:**
```bash
curl -X POST http://localhost:8000/api/v1/amazon/sync \
  -H "Authorization: Bearer <token>"
```

## Default Credentials

For development, seed data includes:
- **Admin**: username: `admin`, password: `admin123`
- **User**: username: `user`, password: `user123`

**Note**: Change these credentials in production.

## Project Structure

```
app/
├── api/v1/               # API endpoints
│   └── endpoints/        # Route modules (products, suppliers, etc.)
├── core/                 # Configuration, database, security
├── db/                   # Database sessions and models
├── integrations/         # Third-party integrations (Amazon, CSV)
├── models/               # SQLAlchemy ORM models
├── schemas/              # Pydantic request/response schemas
├── tasks/                # Celery background tasks
└── main.py              # FastAPI application entry point
scripts/                  # Database initialization and testing scripts
templates/                # Sample CSV templates for imports
```

## Environment Variables

Required variables in `.env`:
```
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=<your-secret-key>
AMAZON_REFRESH_TOKEN=<token>
AMAZON_CLIENT_ID=<id>
AMAZON_CLIENT_SECRET=<secret>
AWS_ACCESS_KEY=<key>
AWS_SECRET_KEY=<secret>
AMAZON_MARKETPLACE_ID=ATVPDKIKX0DER
CORS_ORIGINS=["http://localhost:3000"]
```

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

MIT
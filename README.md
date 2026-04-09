# Procurement-Roger

A comprehensive FastAPI-based procurement management system with inventory tracking, purchase order management, and Amazon Selling Partner API integration. Streamline procurement workflows with CSV import/export, automated inventory syncing, and async task processing.

## Features

- **RESTful API** - Built with FastAPI with comprehensive OpenAPI/Swagger documentation
- **Inventory Management** - Track products, inventory movements, and stock levels
- **Purchase Order System** - Create, manage, and track purchase orders and suppliers
- **Amazon Integration** - Sync orders and inventory with Amazon Selling Partner API
- **CSV Import/Export** - Bulk import products, inventory, and purchase orders via CSV
- **Async Processing** - Background task queue with Celery for heavy operations
- **Authentication** - User authentication and role-based access control
- **Database Management** - SQLAlchemy ORM with initialization and seeding scripts

## Tech Stack

- **Framework**: FastAPI
- **Database**: SQLAlchemy ORM (SQLite by default, configurable)
- **Task Queue**: Celery
- **CSV Processing**: Pandas
- **Amazon API**: Python SP-API library
- **Auth**: JWT tokens with bcrypt password hashing

## Setup

1. **Clone and enter the directory**
   ```bash
   git clone https://github.com/your-username/procurement-roger.git
   cd procurement-roger
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your database URL, Amazon API credentials, etc.
   ```

5. **Initialize database**
   ```bash
   python scripts/init_db.py
   python scripts/seed_data.py
   ```

6. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`. Access API docs at `/docs` and `/redoc`.

## Usage Example

**List Products**
```bash
curl -H "Authorization: Bearer <token>" \
  http://localhost:8000/api/v1/products
```

**Import Products from CSV**
```bash
POST /api/v1/tasks/import-products
Content-Type: application/json

{"file_path": "templates/products.csv"}
```

**Create Purchase Order**
```bash
POST /api/v1/purchase-orders
Content-Type: application/json

{
  "supplier_id": 1,
  "po_number": "PO-2024-001",
  "items": [{"product_id": 1, "quantity": 10, "unit_price": 25.00}]
}
```

## Project Structure

- `app/api/v1/endpoints/` - API route handlers (products, purchase orders, inventory, suppliers, auth)
- `app/integrations/` - Third-party integrations (Amazon SP-API, CSV import)
- `app/models/` - SQLAlchemy data models
- `app/schemas/` - Pydantic request/response schemas
- `app/tasks/` - Celery async tasks
- `scripts/` - Database initialization and seeding
- `templates/` - CSV import templates and examples
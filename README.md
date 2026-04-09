# Procurement Management System

A full-stack procurement and inventory management platform with Amazon Seller Central integration, purchase order tracking, and CSV import/export capabilities.

## Features

- **Inventory Management** – Track product SKUs, stock levels, costs, and minimum quantities
- **Purchase Orders** – Create and manage supplier purchase orders with order tracking
- **Supplier Management** – Maintain supplier information and contact details
- **Amazon Integration** – Sync orders, inventory, and products with Amazon Seller Central using SP-API
- **CSV Import/Export** – Bulk import products, inventory movements, and purchase orders from CSV
- **User Authentication** – Secure login and role-based access control
- **REST API** – Complete RESTful API for all operations
- **Real-time Dashboard** – Monitor inventory levels, recent orders, and system health

## Tech Stack

**Backend:**
- FastAPI – Modern Python web framework
- SQLAlchemy – ORM for database operations
- Celery – Background task processing
- Pandas – CSV file processing
- Amazon SP-API – Seller Central integration

**Frontend:**
- React 18 with TypeScript
- Vite – Fast build tool
- Tailwind CSS – Utility-first styling
- React Router – Client-side routing

**Database:**
- SQLite (development) / PostgreSQL (production-ready)

## Setup

### Backend

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

4. Initialize the database:
   ```bash
   python scripts/init_db.py
   ```

5. Start the API server:
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000` with interactive docs at `/docs`.

### Frontend

1. Navigate to the frontend directory:
   ```bash
   cd Proc2/procurement-frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Open `http://localhost:5173` in your browser

### Background Tasks (Celery)

```bash
celery -A app.worker worker --loglevel=info
```

## Usage

### API Endpoints

- `POST /api/v1/auth/login` – Authenticate user
- `GET /api/v1/products` – List all products
- `POST /api/v1/products` – Create new product
- `GET /api/v1/suppliers` – List suppliers
- `GET /api/v1/purchase-orders` – List purchase orders
- `GET /api/v1/inventory` – List inventory movements
- `POST /api/v1/amazon/sync` – Sync Amazon orders and inventory

### CSV Import

Place CSV files in `templates/` directory with proper column headers:

**products.csv:**
```
sku,name,description,price,cost,quantity,min_quantity,asin
TEST-001,Product Name,Description,99.99,49.99,100,10,B001EXAMPLE
```

**purchase_orders.csv:**
```
po_number,supplier_id,status,total_amount,currency,expected_delivery_date
PO-2024-001,1,draft,500.00,USD,2024-04-30
```

Then use the import API endpoints to process the files.

## Configuration

Key environment variables (see `.env`):

```
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your-secret-key-here
AMAZON_REFRESH_TOKEN=your-amazon-token
AMAZON_CLIENT_ID=your-client-id
AMAZON_CLIENT_SECRET=your-client-secret
AWS_ACCESS_KEY=your-aws-access-key
AWS_SECRET_KEY=your-aws-secret-key
AMAZON_MARKETPLACE_ID=ATVPDKIKX0DER
CORS_ORIGINS=http://localhost:5173,http://localhost:3000
```

## Project Structure

```
├── app/                          # Backend application
│   ├── api/v1/                   # API endpoints
│   ├── integrations/             # Amazon SP-API and CSV import
│   ├── models/                   # SQLAlchemy models
│   ├── schemas/                  # Pydantic schemas
│   ├── tasks/                    # Celery tasks
│   ├── core/                     # Config, database, security
│   └── main.py                   # FastAPI app entry point
├── Proc2/procurement-frontend/   # React frontend
│   ├── src/
│   │   ├── components/           # React components
│   │   ├── pages/                # Page components
│   │   ├── services/             # API service calls
│   │   ├── stores/               # State management
│   │   └── App.tsx               # Main app component
│   └── package.json
├── scripts/                      # Utility scripts
├── templates/                    # CSV import templates
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## License

MIT
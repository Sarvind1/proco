# Procurement System

A comprehensive procurement and inventory management platform with Amazon Seller Partner API integration. Manage products, purchase orders, suppliers, and inventory movements through an intuitive web interface with CSV import/export capabilities.

## Features

- **Procurement Management** - Create and manage purchase orders with supplier tracking
- **Inventory Management** - Track inventory levels, movements, and stock alerts
- **Amazon Integration** - Sync orders, inventory, and products with Amazon Seller Central
- **CSV Import/Export** - Bulk import products, inventory, and purchase orders from CSV
- **User Authentication** - Secure login with role-based access control
- **RESTful API** - Full-featured FastAPI backend with OpenAPI documentation
- **Real-time Dashboard** - Interactive React frontend with responsive design
- **Async Tasks** - Background task processing with Celery for bulk operations

## Tech Stack

**Backend:**
- FastAPI
- SQLAlchemy ORM
- Celery (async tasks)
- Amazon Seller Partner API
- PostgreSQL/SQLite

**Frontend:**
- React 18
- TypeScript
- Vite
- Tailwind CSS
- TanStack Table

## Setup

### Backend

1. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables in `.env`:
```
DATABASE_URL=sqlite:///./test.db
AMAZON_CLIENT_ID=your_amazon_client_id
AMAZON_CLIENT_SECRET=your_amazon_client_secret
AMAZON_REFRESH_TOKEN=your_refresh_token
AWS_ACCESS_KEY=your_aws_key
AWS_SECRET_KEY=your_aws_secret
AMAZON_MARKETPLACE_ID=ATVPDKIKX0DER
```

4. Run the API server:
```bash
python -m uvicorn app.main:app --reload
```

API docs available at `http://localhost:8000/docs`

### Frontend

1. Navigate to the frontend directory:
```bash
cd Proc2/procurement-frontend
```

2. Install dependencies:
```bash
npm install
```

3. Configure environment in `.env`:
```
VITE_API_URL=http://localhost:8000/api/v1
```

4. Start the development server:
```bash
npm run dev
```

## Usage

1. **Login**: Access the frontend at `http://localhost:5173` and login with default credentials
2. **Create Products**: Navigate to Products page and add items or import from CSV
3. **Manage Suppliers**: Add suppliers in the Suppliers section
4. **Create Purchase Orders**: Create POs linked to suppliers and products
5. **Track Inventory**: Monitor inventory levels and movement history
6. **Amazon Sync**: Connect Amazon account in Settings and sync orders/inventory

## API Endpoints

- `POST /api/v1/auth/login` - User authentication
- `GET/POST /api/v1/products` - Product management
- `GET/POST /api/v1/suppliers` - Supplier management
- `GET/POST /api/v1/purchase-orders` - Purchase order operations
- `GET/POST /api/v1/inventory` - Inventory tracking
- `GET /api/v1/amazon/orders` - Amazon order sync

## Development

- Backend tests: `pytest`
- Frontend tests: `npm run test`
- Linting: Backend with `pylint`, Frontend with `npm run lint`
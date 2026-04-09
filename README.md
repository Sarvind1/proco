# Procurement System

A full-stack procurement and inventory management system with Amazon sales integration. Manage products, purchase orders, suppliers, and inventory movements. Includes CSV import/export and real-time Amazon seller central data synchronization.

## Features

- **Product Management** - Track products with SKU, ASIN, pricing, and inventory levels
- **Purchase Orders** - Create and manage purchase orders with line-item tracking
- **Supplier Management** - Maintain supplier contact information and availability
- **Inventory Tracking** - Monitor inventory movements, stock levels, and reorder thresholds
- **Amazon Integration** - Sync orders and inventory data with Amazon Seller Central via SP-API
- **CSV Import/Export** - Bulk import products and inventory, export data for reporting
- **User Authentication** - Role-based access control (admin and regular users)
- **Dashboard** - Real-time view of procurement metrics and inventory status
- **Async Tasks** - Background job processing with Celery for imports and syncs

## Tech Stack

**Backend:**
- FastAPI (Python web framework)
- SQLAlchemy ORM with SQLite database
- Celery for async task queue
- Amazon SP-API integration
- Pandas for CSV processing

**Frontend:**
- React 18 with TypeScript
- Vite (build tool)
- Tailwind CSS for styling
- Axios for API calls

## Setup

### Backend Setup

1. Install Python dependencies:
   ```bash
   cd app
   pip install -r requirements.txt
   ```

2. Create and configure `.env` file:
   ```
   DATABASE_URL=sqlite:///./test.db
   SECRET_KEY=your-secret-key
   AMAZON_CLIENT_ID=your-amazon-client-id
   AMAZON_CLIENT_SECRET=your-amazon-secret
   AMAZON_REFRESH_TOKEN=your-refresh-token
   AWS_ACCESS_KEY=your-aws-key
   AWS_SECRET_KEY=your-aws-secret
   ```

3. Initialize the database and seed sample data:
   ```bash
   python scripts/seed_data.py
   ```

4. Start the FastAPI server:
   ```bash
   python -m uvicorn app.main:app --reload
   ```

5. Start Celery worker (optional, for background tasks):
   ```bash
   celery -A app.worker worker --loglevel=info
   ```

### Frontend Setup

1. Install Node dependencies:
   ```bash
   cd Proc2/procurement-frontend
   npm install
   ```

2. Create `.env` file:
   ```
   VITE_API_URL=http://localhost:8000/api/v1
   ```

3. Start development server:
   ```bash
   npm run dev
   ```

API documentation available at `http://localhost:8000/docs` (Swagger UI)

## Usage

### Access the Application

- **Frontend:** http://localhost:5173
- **API Docs:** http://localhost:8000/docs
- **Default credentials:** username: `admin`, password: `admin123`

### Import Products from CSV

Upload a CSV file with columns: `sku`, `name`, `price`, `cost`, `quantity`, `min_quantity`, `asin` (optional)

### Sync Amazon Data

The system automatically syncs orders and inventory from Amazon on a scheduled interval. Manual sync available via the dashboard.

### Export Inventory Report

Generate CSV exports of current inventory, purchase orders, and supplier information from the dashboard.

## Project Structure

```
.
├── app/                          # FastAPI backend
│   ├── api/v1/                  # API endpoints
│   ├── models/                  # SQLAlchemy models
│   ├── schemas/                 # Pydantic schemas
│   ├── integrations/            # Amazon SP-API, CSV handling
│   ├── tasks/                   # Celery async tasks
│   └── core/                    # Config, security, database
├── Proc2/procurement-frontend/   # React frontend
│   ├── src/
│   │   ├── pages/              # Page components
│   │   ├── components/         # UI components
│   │   ├── services/           # API client services
│   │   └── stores/             # State management
│   └── package.json
├── scripts/                     # Utility scripts
└── templates/                   # CSV import templates
```

## Notes

- Ensure all environment variables are configured before running
- Use a real database (PostgreSQL recommended) for production instead of SQLite
- Rotate AWS and Amazon API credentials regularly
- Configure CORS origins in production environment
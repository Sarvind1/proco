from celery.schedules import crontab
from app.worker import celery_app
from app.tasks.amazon_sync import sync_amazon_orders, sync_amazon_inventory

# Configure periodic tasks
celery_app.conf.beat_schedule = {
    "sync-amazon-orders": {
        "task": "app.tasks.amazon_sync.sync_amazon_orders",
        "schedule": crontab(minute="*/15"),  # Every 15 minutes
    },
    "sync-amazon-inventory": {
        "task": "app.tasks.amazon_sync.sync_amazon_inventory",
        "schedule": crontab(minute="*/30"),  # Every 30 minutes
    },
} 
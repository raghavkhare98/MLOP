import os
import django
import time
from datetime import datetime, timedelta
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VETL.settings')
django.setup()

from product.models import Product 

CATEGORIES = ['Electronics', 'Books', 'Grocery', 'Toys', 'Clothing'] 
VENDORS = {
    'Electronics': ['samsung', 'apple', 'sony', 'intel', 'msi'],
    'Books': ['Penguin Random House', 'HarperCollins', 'Simon & Schuster', 'Hachette Book Group', 'Macmillan Publishers'],
    'Grocery': ['Nestle', 'Unilever', 'Walmart', 'PepsiCo', 'Kellogs'],
    'Toys': ['LEGO', 'Hasbro', 'Spinmaster', 'Mattel', 'EA'],
    'Clothing': ['H&M', 'Levis', 'Reliance Trends', 'Gymshark', 'Puma']
}

def create_random_product():
    now = datetime.now()
    product_category_choice = random.choice(CATEGORIES)
    product_vendor_choice = random.choice(VENDORS[product_category_choice])
    product = Product.objects.create(
        product_name=f"Product_{int(time.time())}",
        product_category=product_category_choice,
        product_mfg_date=now,
        product_expiry_date=now + timedelta(days=random.randint(30, 365)),
        product_price=random.randint(1, 1000),
        product_vendor=product_vendor_choice
    )
    print(f"Inserted: {product.product_name} at {now}")
 
if __name__ == '__main__':
    print("Starting product insertion every 5 seconds. Press Ctrl+C to stop.")
    try:
        while True:
            create_random_product()
            time.sleep(5)
    except KeyboardInterrupt:
        print("Stopped by user.")


#TODO: Create a large dataset. Preferrably 20k rows and expose the backend API throug ngrok
#TODO: Logging. We have to save logs of events and perform dblogging
#TODO: Python script to export csv from the DB
#TODO: Integrate a NoSQL DB in django settings
#TODO: Provide different queries/filters using pandas. You can filter and show the products
#TODO: Implement a service layer for connection of multiple DBs like mysql, and a nosql (mongodb, elasticdb)


#!/bin/bash

echo "==> Migrating to the db"
python manage.py makemigrations
python manage.py migrate

echo "==> Loading product fixtures..."
python manage.py loaddata products/fixtures/product_model.json

echo "==> Loading category fixtures..."
python manage.py loaddata products/fixtures/category.json

echo "==> Loading unit fixtures..."
python manage.py loaddata products/fixtures/unit.json


echo "==> Loading expense fixtures..."
python manage.py loaddata expense/fixtures/expense.json

echo "==> Loading expense category fixtures..."
python manage.py loaddata expense/fixtures/expense_category.json

echo "==> Loading customer fixtures..."
python manage.py loaddata customers/fixtures/customer.json

echo "==> Loading suppliers fixtures..."
python manage.py loaddata suppliers/fixtures/suppliers.json

echo "==> Loading account fixtures..."
python manage.py loaddata accounts/fixtures/bank_account_model.json

echo "==> Loading sale fixtures..."
python manage.py loaddata sales/fixtures/sales_model.json



echo "==> Done!"

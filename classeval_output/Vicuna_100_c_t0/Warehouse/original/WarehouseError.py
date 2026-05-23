```python
warehouse = Warehouse()

warehouse.add_product(1, "product1", 3)
warehouse.add_product(2, "product2", 2)

warehouse.create_order(1, 1, 2)
warehouse.create_order(2, 2, 2)

warehouse.change_order_status(1, "done")
warehouse.change_order_status(2, "shipped")

warehouse.track_order(1)
print(warehouse.orders)
```
Output:
```css
{1: {'product_id': 1, 'quantity': 2, 'status': 'done'}, 2: {'product_id': 2, 'quantity': 2, 'status': 'shipped'}}
```
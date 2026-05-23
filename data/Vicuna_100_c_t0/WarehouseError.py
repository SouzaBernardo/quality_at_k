warehouse = Warehouse()

warehouse.add_product(1, "product1", 3)
warehouse.add_product(2, "product2", 2)

warehouse.create_order(1, 1, 2)
warehouse.create_order(2, 2, 2)

warehouse.change_order_status(1, "done")
warehouse.change_order_status(2, "shipped")

warehouse.track_order(1)
print(warehouse.orders)
nylon_qty_sqr_meters = int(input())
paint_qty_litres = int(input())
thinner_qty_litres = int(input())
hours_to_complete = int(input())
total_amount_products = \
                (nylon_qty_sqr_meters + 2) * 1.5 \
                + (paint_qty_litres * (1 + 0.1) * 14.5) \
                + (thinner_qty_litres * 5) \
                + 0.4
total_amount_work = total_amount_products * 0.3 * hours_to_complete
total_amount = total_amount_work + total_amount_products
print(f'{total_amount}')

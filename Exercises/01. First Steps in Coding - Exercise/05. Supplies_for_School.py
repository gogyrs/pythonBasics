num_pen_packages = int(input())
num_marker_packages = int(input())
board_clean_liquid_litres = int(input())
discount_percentage = int(input())
total_amount = num_pen_packages * 5.8 \
               + num_marker_packages * 7.2 \
               + board_clean_liquid_litres * 1.2
total_amount_with_discount = total_amount * (1 - discount_percentage/100)
print(total_amount_with_discount)

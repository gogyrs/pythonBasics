chicken_menu_count = int(input())
fish_menu_count = int(input())
veggie_menu_count = int(input())
total_menu_prize = chicken_menu_count * 10.35 \
                    + fish_menu_count * 12.40 \
                    + veggie_menu_count * 8.15
dessert_prize = total_menu_prize * 0.2
total_prize = total_menu_prize + dessert_prize + 2.50
print(f'{total_prize}')

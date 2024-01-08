annual_prize = int(input())
basketball_sneakers_prize = annual_prize * (1 - 0.4)
basketball_equipment_prize = basketball_sneakers_prize * (1 - 0.2)
basketball_ball_prize = basketball_equipment_prize * 0.25
basketball_accessories_prize = basketball_ball_prize * 0.2
total_prize = annual_prize + basketball_accessories_prize + basketball_equipment_prize \
              + basketball_ball_prize + basketball_sneakers_prize
print(total_prize)

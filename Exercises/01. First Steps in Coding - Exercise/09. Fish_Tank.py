length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent = float(input())
volume_cm = length_cm * width_cm * height_cm
real_volume_cm = volume_cm * (1 - percent/100)
litres_needed = real_volume_cm / 1000
print(litres_needed)

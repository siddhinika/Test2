length = float(input('Enter the wall length:'))
height = float(input('Enter the wall height:'))
rate = float(input('Enter the wall rate of painting per meter:'))

area = length * height
total_area = area * 4
total_cost = total_area * rate 

print(f'Total painting cost is:{total_cost}')
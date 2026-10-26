radius = 20
length = 50
breadth = 40
cost_per_meter = 35
fencing_time = 5
pi = 3.14

perimeter = (pi * radius) + (2 * length) + breadth
total_wire = perimeter * fencing_time
total_cost = total_wire * cost_per_meter

print(f'The total cost is:{total_cost}')
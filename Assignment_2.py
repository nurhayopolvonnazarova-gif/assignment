def classify(value):
    if value < 98:
        return "Below range"
    elif value <= 102:
        return "In range"
    else:
        return "Above range"


def calculate_average(total, count):
    average_snapshot = total / count
    average_result = average_snapshot
    return average_result


number_of_tiles = int(input("Enter the number of tiles: "))

total_width = 0
below_range_count = 0
in_range_count = 0
above_range_count = 0

for i in range(number_of_tiles):
    width = int(input("Enter the tile width: "))

    classification = classify(width)
    print(classification)

    total_width += width

    if classification == "Below range":
        below_range_count += 1
    elif classification == "In range":
        in_range_count += 1
    else:
        above_range_count += 1

average_width = calculate_average(total_width, number_of_tiles)

print(f"Total width: {total_width} mm")
print(f"Average width: {average_width} mm")
print(f"Below range: {below_range_count}")
print(f"In range: {in_range_count}")
print(f"Above range: {above_range_count}")

def rectangleArea(length, width):
    area = length * width
    return area

area1 = rectangleArea(10,6)
print("Rectangle 1:")
print(f"Length: 10")
print(f"Width: 6")
print(f"Area: {area1}")
if area1 < 50:
    print("Size: Large Rectangle")
    
area2 = rectangleArea(50,36)
print("Rectangle 2:")
print(f"Length: 10")
print(f"Width: 6")
print(f"Area: {area1}")
if area2 > 50:
    print("Size: Large Rectangle")
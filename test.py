import matplotlib.pyplot as plt

# Tọa độ điểm A
x1, y1 = 1, 2

# Tọa độ điểm B
x2, y2 = 5, 6

# Tính độ dốc (slope) của đoạn thẳng
dx = x2 - x1
dy = y2 - y1

# Xác định bước đi
steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

# Tính giá trị thay đổi cho x và y
x_increment = dx / steps
y_increment = dy / steps

# Khởi tạo danh sách lưu trữ các điểm trên đoạn thẳng
points = []

# Tạo danh sách các điểm trên đoạn thẳng
for i in range(int(steps) + 1):
    points.append((round(x1), round(y1)))
    x1 += x_increment
    y1 += y_increment

# Vẽ đoạn thẳng bằng matplotlib
x_values, y_values = zip(*points)
plt.plot(x_values, y_values)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Vẽ đoạn thẳng từ A đến B')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import GA

###本实现采用了第3方库pybind11，该版本只能在macOS上运行，在windows系统上需要重新编译cpp文件生成.pyd文件


#调用c++编写的遗传算法
maxGen = 10000
result = GA.solution_from_cpp(maxGen)

cities = {city.num: (city.x, city.y) for city in result.city_loc}

# 路径图
path = result.best_path
x_coords = [cities[city_num][0] for city_num in path]
y_coords = [cities[city_num][1] for city_num in path]

plt.figure(figsize=(10, 6))
plt.scatter(x_coords, y_coords, c='red', marker='o')
plt.plot(x_coords, y_coords, c='blue')

for city_num in path:
    plt.annotate(city_num, (cities[city_num][0], cities[city_num][1]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.title('TSP Path')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')

# 最优个体统计图
best_individuals = result.best_individuals

plt.figure(figsize=(10, 6))

plt.plot(best_individuals)
plt.title('Best Individual Distance per Generation')
plt.xlabel('Generation')
plt.ylabel('Distance')
plt.grid(True)
plt.show()
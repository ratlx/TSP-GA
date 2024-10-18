cmake_minimum_required(VERSION 3.29)
project(TSP_GA)

set(CMAKE_CXX_STANDARD 14)

# 查找 Python3
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)

# 查找 pybind11
find_package(pybind11 REQUIRED)

# 将 Python3 的包含路径添加到 include_directories
#include_directories(${Python3_INCLUDE_DIRS} /Users/louxu/miniconda3/include)

# 添加模块库
#add_library(tsp_ga MODULE TSP-GA.cpp)
pybind11_add_module(GA TSP-GA.cpp)

target_compile_options(GA PRIVATE -O3)

#set_target_properties(tsp_ga PROPERTIES SUFFIX ".so")

# 确保可执行文件也链接到 Python 和 pybind11
#target_link_libraries(tsp_ga PRIVATE Python3::Python pybind11::module)


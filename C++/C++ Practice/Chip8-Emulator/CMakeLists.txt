cmake_minimum_required(VERSION 3.14)
project(chip8)

set(CMAKE_CXX_STANDARD 11)

find_package(SDL2 REQUIRED)

add_executable(
    chip8
    chip8.cpp
    main.cpp
    platform.cpp)

target_compile_options(chip8 PRIVATE -Wall)

target_link_libraries(chip8 PRIVATE SDL2::SDL2)
cmake_minimum_required(VERSION 3.10)
project(gtk_test)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(PkgConfig REQUIRED)
pkg_check_modules(GTK4 REQUIRED IMPORTED_TARGET gtk4)

add_executable(gtk_test hello-world-gtk.c)
target_link_libraries(gtk_test PRIVATE PkgConfig::GTK4)

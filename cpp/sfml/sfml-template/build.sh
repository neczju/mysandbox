#! /bin/sh
g++ -c main.cpp -I sfml
g++ main.o -o sfml-app -L sfml -lsfml-graphics -lsfml-window -lsfml-system

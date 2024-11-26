#! /bin/sh
g++ -c main.cpp -I sfml
g++ main.o -o rpg -L sfml -lsfml-graphics -lsfml-window -lsfml-system

#!/usr/bin/env python3

r1 = ["◽","◽","◽"]
r2 = ["◽","◽","◽"]
r3 = ["◽","◽","◽"]

map_row = [r1,r2,r3]

print(f"{r1}\n{r2}\n{r3}")
location = input("Where do you want to put the treasure? ")

location1 = int(location[0]) - 1
location2 = int(location[1]) - 1

map_row[location1][location2] = "x"


print(f"{r1}\n{r2}\n{r3}")

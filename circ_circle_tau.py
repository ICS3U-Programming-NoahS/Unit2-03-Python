#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Sept. 27th, 2023
# This program asks the user for the radius of
# a circle in cm. It then calculates and displays
# the circumference using TAU.
import constants


def main():
    # get the radius from the user
    radius = float(input("Enter the radius of the circle (cm): "))

    # calculate the circumference
    circumference = constants.TAU * radius

    # display the circumference back to the user
    print("")
    print("Circumference = {:.2f} cm".format(circumference))


if __name__ == "__main__":
    main()

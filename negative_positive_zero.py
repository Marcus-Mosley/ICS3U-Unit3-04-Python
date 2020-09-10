#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on September 2020
# This program checks if an integer is negative, positive, or zero


def main():
    # This function checks if an integer is negative, positive, or zero

    # Input
    integer = int(input("Enter an Integer: "))
    print("")

    # Process & Output
    if integer > 0:
        print("This integer is + (positive)!")
    elif integer < 0:
        print("This integer is - (negative)!")
    else:
        print("This integer is 0 (zero)!")


if __name__ == "__main__":
    main()

#Shelly Wang
#Oct 17,2023
#purpose: to get a prism’s total surface area
#last correction: 1/19/2024


def printInstructions():
    """this function takes no paramters are prints out instructions to the users;returns:none"""
    print("please input the length, width, and height of the solid")
    print("This program computes the surface area of a rectangular prism")



def areaRectangle(side1, side2):
    rectangle_area = side1*side2
    return rectangle_area                                                                   # use return to invoke areaRactangle
                                                                                                # Use def to figure out the area of one side and then go back
def totalSurfaceArea(l,w,h):                                                                    # to make a new function

    areaRectangle(l, w)
    areaRectangle(l, h)
    areaRectangle(w, h)

    area=int(areaRectangle(l, w))*2+int(areaRectangle(l, h))*2+int(areaRectangle(w, h))*2
    return area                                                                                 # use return to invoke area, and it can to make the function correct
                                                                                                #  You figure out the three sides, and then you multiply by 2 and that's its surface area
def printResult(result):
    print("THe surface area is",result)
                                                                                                # 'print' to get the answer
def ask_length():                                                                               # to make a new function ask a length, width and height
    l = int(input("What is the length: "))
    return l

def ask_width():
    w = int(input("What is the width: "))
    return w

def ask_height():
    h = int(input("What is the height: "))
    return h
                                                                                                # to ask user how many length, width and height do there have?
def main():
    printInstructions()
    l = ask_length()
    w = ask_width()
    h = ask_height()
    result = totalSurfaceArea(l, w, h)
    printResult(result)
                                                                                                #  To call all the previous ones function
main()

#test
#test









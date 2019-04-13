
""" 
    @Author: Taylor
    @version: 1.0
    @function: 画五角星
"""
import turtle


def main():    
    count = 0
    while count < 5:
        turtle.forward(100)
        turtle.right(144)
        count+=1

    turtle.exitonclick()
        
    



if __name__ == "__main__":
    main()
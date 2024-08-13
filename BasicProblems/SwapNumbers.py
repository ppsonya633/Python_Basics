# author: Pratik Patil
# date: 12-08-2024
# title: Swapping of numbers


def swap(x,y):
    print("Before Swapping x:",x)
    print("Before Swapping y:",y)
    x,y=y,x
    print("After Swapping x:",x)
    print("After Swapping y:",y)

def main():
  x=10
  y=20
  swap(x,y)

main()
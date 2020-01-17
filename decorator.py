# def christmasTree(func):
#     print("It's a Tree ")
#     def my_wrap(color): #需要定義一個fucntion當wrapper，不然compiler會說不知道那個
#         func(color)
#     return my_wrap

# @christmasTree  #這個是大機器
# def star(color):    #大機器中的小格子可以自己定義放東西進去
#     print(f"with a {color} star on it.")

# star('red')


def returnItself():
    print("I returned myself.")

def functioncaller(func):
    func()

functioncaller(returnItself)
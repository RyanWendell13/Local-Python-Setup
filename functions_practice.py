def hello():
    print("hello")

def pack(arg1, arg2, arg3):
    return [arg1,arg2,arg3]

def eat_lunch(list):
    if len(list) > 0:
        first = True
        for i in list:
            if first == False:
                print("Next I eat "+i)
                
            else:
                print("First I eat "+i)
                first = False
    else:
        print("My lunchbox is empty")


hello()
print(pack("1","2","3"))

eat_lunch([])
eat_lunch(["1","2","3"])
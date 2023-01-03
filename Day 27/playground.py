def add(*args):
# args give unlimited arguments
# turns arguments into tuple
    sum=0
    for n in args:
        sum+=n
    print(sum)
# add(2,3,4,5)

def calc(num,**kwargs):
    # kwargs stand for keyworded arguments
    # turns arguments into dictionary
    num+=kwargs["a"]
    print(num)
    num*=kwargs["b"]
    print(num)

    num-=kwargs['c']
    print(num)


calc(num=1,a=2,b=3,c=4)

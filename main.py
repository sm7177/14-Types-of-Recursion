#tail recursion

# def tail(n):
#     if(n!=0):
#         print(n)
#         tail(n-1)
        
# x=4
# tail(x)




#head recursion

# def head(n):
#     if(n!=0):
#         head(n-1)
#         print(n)
        
# x=4
# head(x)





# #tree recursion
# def tree(n):
#     if(n!=0):
#         print(n)
#         tree(n-1)
#         tree(n-1)
        
# x=2
# tree(x)






#indirect recursion
def funA(n):
    if(n>0):
        print("",n,end='')
        funB(n-1)
        
def funB(n):
    if(n>1):
        print("",n,end='')
        
        funA(n//2)
        
funA(20)
              
              
        
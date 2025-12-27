def main():
    
    a,b = map(int,input().split())
    def f (a, b):
        r = (a+b)*(a-b)
        return r
    
    result = f(a, b)
    print (result)
        
    
    
if __name__ == '__main__':
    main()
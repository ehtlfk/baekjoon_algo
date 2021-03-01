def main():
    
    def reculsive(n,k,t):
        
        if n == k: 
            return t
        else:
            reculsive(n+1,k,t+n+1)
            
    
    print(reculsive(0,3,0))
if __name__ == "__main__":
    main()


import random as r

def main():
    numbers = []
    m_dict = {}
    
    def gamble():
        while len(numbers) < range(6):
            nr = r.randint(44)
            
            if(nr not in numbers):
                numbers.append(nr)
        
    
    
    
    
    
    
    
if __name__ == "main":
    main()
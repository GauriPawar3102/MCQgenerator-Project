
# Python program to illustrate  
# closures  
import logging  
logging.basicConfig(filename ='example.log', level = logging.INFO)  
    
#Logger function to find the logs of arguments  
def logger(func):  
    def log_func(*args):  
        logging.info(  
            'Running "{}" with arguments {}'.format(func.__name__, args))  
        print(func(*args))  
    # Necessary for closure to work (returning WITHOUT parenthesis)  
    return log_func                
    
def add(x, y):           #adding the values
    return x + y  
    
def sub(x, y):           #subtracting two values
    return x-y  
    
add_logger = logger(add)  
sub_logger = logger(sub)  
    
add_logger(3, 3)  
add_logger(4, 5)  
    
sub_logger(10, 5)  
sub_logger(20, 10)  


#This is the python program for functions inside function

#File has been successfully updated

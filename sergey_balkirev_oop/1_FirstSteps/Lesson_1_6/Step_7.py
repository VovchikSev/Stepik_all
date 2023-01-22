class SingletonFive:
    __instance = None
    __count = 0
    def __new__(cls, *args, **kwargs):
        if cls.__count < 5:
            cls.__instance = super().__new__(cls)
            cls.__count += 1
        
        return cls.__instance
        
    
    def __init__(self, num_str):
        self.name = num_str
    

# n = 10
objs = [SingletonFive(str(n)) for n in range(10)] # эту строчку не менять
class Human ():
    def __init__(self):
        pass
    
class Man (Human):
    def __init__(self,name):
        self.name=name
    
class Woman (Human):
    def __init__(self,name):
        self.name=name
    

def God():
    man = Man('Adam')
    woman = Woman('Eva')
    return [man, woman]




# def God():
#     return [Man(), Woman()]

# class Human(object):
#     pass

# class Man(Human):
#     pass
    
# class Woman(Human):
#     pass
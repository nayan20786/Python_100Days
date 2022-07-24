# Day 21:: Inheritance

class Animal:
    def __init__(self):
        self.length = 20

    def breathe(self):
        print("inhale,Exhale")


class fish(Animal):
    def __init__(self):
        super(fish, self).__init__()

    def breathe(self):
        """
        Here i Inherited the Breathe method in fish class from Animal and
        add a little more functionality to it
        :return:
        """
        super(fish, self).breathe()
        print("Lalalalal")

    def swim(self):
        print("Fish swims in water")


nemo = fish()

nemo.swim()
nemo.breathe()
print(nemo.length)

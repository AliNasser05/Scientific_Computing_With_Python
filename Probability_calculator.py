import random
import copy

class Hat:
    def __init__(self, **kwargs):
        self.contents = []

        for name, count in kwargs.items():
            cnt = count
            while cnt > 0:
                self.contents.append(name)
                cnt -= 1

    def draw(self, number):
        result_list = []
        if len(self.contents) < number:
            result_list = self.contents.copy()
            self.contents = []
            return result_list

        while len(result_list) < number:
            value = random.choice(self.contents)
            result_list.append(value)
            self.contents.remove(value)

        return result_list
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count_valid = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        valid = True
        colors_value = {}
        colors_list = hat_copy.draw(num_balls_drawn)
        for color in colors_list:
            try:
                colors_value[color] += 1
            except: # if it is the first time the color shows
                colors_value[color] = 1

        for color, count in expected_balls.items():
            try:
                if colors_value[color] < count:
                    valid = False
                    break
            except: # if it is the first time the color shows
                valid = False
                break
        
        if valid:
            count_valid += 1

    return count_valid / num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                        expected_balls={'red':2,'green':1},
                        num_balls_drawn=5,
                        num_experiments=2000)

print(probability)

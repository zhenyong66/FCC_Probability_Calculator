import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.names = []
        self.contents = []
        self.dict = {}
        for key, value in kwargs.items():
            self.names.append(key)
            self.dict[key] = value 
        self.total_balls = 0
        for name in self.names:
            self.total_balls += self.dict[name]
            for i in range(self.dict[name]):
                self.contents.append(name)
    
    def draw(self, num_balls):
        self.num_balls = num_balls
        hat = self.contents
        ball_drawn = []
        if num_balls >= self.total_balls:
            for i in range(self.total_balls):
                num = random.randint(0,len(hat)-1)
                ball_drawn.append(hat[num]) 
                hat.pop(num)
        elif num_balls < self.total_balls:
            for i in range(num_balls):
                num = random.randint(0,len(hat)-1)
                ball_drawn.append(hat[num]) 
                hat.pop(num)
        return ball_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for num_exp in range(num_experiments):
        balls = copy.deepcopy(hat)
        balls_drawn = balls.draw(num_balls_drawn)
        ball_names = []
        balls_drawn_dict = {}
        for key in balls.names:
            ball_names.append(key)
        for name in ball_names:
            num_balls = balls_drawn.count(name)
            balls_drawn_dict[name] = num_balls
        # expected_names = []
        true_cases = 0
        for key, value in expected_balls.items():
            if balls_drawn_dict[key] >= expected_balls[key]:
                true_cases += 1
            if true_cases == len(expected_balls):
                M += 1
    return M/num_experiments

#%% test
# hat1 = Hat(yellow=3, blue=2, green=6)
# hat2 = Hat(red=5, orange=4)
# hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

# hat = Hat(black=6, red=4, green=3)
# probability = experiment(hat=hat, 
#                   expected_balls={"red":2,"green":1},
#                   num_balls_drawn=5,
#                   num_experiments=2000)
# print(probability)

# hat = Hat(blue=3,red=2,green=6)
# probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
# actual = probability
# expected = 0.272

# hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
# probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
# actual = probability
# expected = 1.0

# print(expected)
# print(actual)
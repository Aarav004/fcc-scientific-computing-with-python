import copy
import random

class Hat:
    def __init__(self, **balls):
        if not balls:
            raise ValueError("Atleast one ball is required")
        else:
            self.balls = balls
        self.contents = []
        for key, value in balls.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self, number_of_balls):
        removed_balls =[]
        if number_of_balls > len(self.contents):
            while self.contents:
                b = self.contents.pop(0)
                removed_balls.append(b)
            
            return removed_balls
        else:
            for i in range(number_of_balls):
                draw_ball = random.choice(self.contents)
                removed_balls.append(draw_ball)
                self.contents.remove(draw_ball)
            return removed_balls

    
    def __str__(self):
        return f"{self.balls}"
   
h1 = Hat(red = 2, blue = 1)
print(h1)
print(f"contents of hat: {h1.contents}")
print(h1.draw(4))
print(h1.contents)




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)

        drawn_balls = hat_copy.draw(num_balls_drawn)

        drawn_ball_count = {}
        for ball in drawn_balls:
            if ball in drawn_ball_count:
                drawn_ball_count[ball] += 1
            else:
                drawn_ball_count[ball] = 1
        
        match = True

        for ball, count in expected_balls.items():
            if drawn_ball_count.get(ball, 0) < count:
                match = False
                break
            match = True
        if match:
            success_count += 1
    return success_count/num_experiments




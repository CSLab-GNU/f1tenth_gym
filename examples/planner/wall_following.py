class WallPlanner:

    def __init__(self, params, robot_scale=0.3302):
        self.parms = params
        self.robot_scale = robot_scale

    def plan(self, obs):
        ranges = obs['scans']
        left = ranges[720]
        

        if left > 2.1:
            steering_angle = 0.15
            speed = 2.0
        elif left < 1.7:
            steering_angle = -0.15
            speed = 2.0
        else:
            steering_angle = 0.0
            speed = 7.0
            
        return speed, steering_angle

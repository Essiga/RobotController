from Behavior import Behavior


class FollowingWall(Behavior):
    def __init__(self):
        super().__init__()
        self.state = "following wall"
        self.speed_factor = 0.5


    def is_applicable(self, robot):
        #always true as it is the last behavior we are checking for
        return True

    def execute(self, robot):
        sensor_values = robot.getProximitySensorValues()

        if(sensor_values[1] < 0.0450 or sensor_values[2] < 0.0450 or sensor_values[3] < 0.0450 or sensor_values[4] < 0.0450 and sensor_values[0] > 0.05):
            robot.setMotorSpeeds(1 * self.speed_factor, - 0.5 * self.speed_factor)
        elif(sensor_values[2] < 0.05 and sensor_values[3] < 0.05):
            robot.setMotorSpeeds(1 * self.speed_factor, 0.75 * self.speed_factor)
        elif(sensor_values[1] > 0.05 or sensor_values[0] > 0.035):
            robot.setMotorSpeeds(0.25 * self.speed_factor, 1 * self.speed_factor)
        else:
            robot.setMotorSpeeds(1 * self.speed_factor, 1 * self.speed_factor)

# Starter Robot Code
import os

import wpilib
from wpilib import TimedRobot

from robotcontainer import RobotContainer
import commands2


class Robot(commands2.TimedCommandRobot):

    def robotInit(self) -> None:
        self.container = RobotContainer()

#DO NOT OVERRIDE TIMED COMMAND ROBOT PERIODIC
    #def robotPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        pass

    def teleopPeriodic(self) -> None:
        #forward = self.container.controller.getRawAxis(0)
        #rotate = self.container.controller.getRawAxis(1)
        #self.container.drivetrain.arcadeDrive(rotate, forward)
        #print(f"Forward: {forward}, Rotate: {rotate}")
        pass

    def autonomousInit(self) -> None:
        # self.auto = self.container.get_autonomous()
        self.auto = self.container.getAuto()

        if self.auto:
            self.auto.schedule()

    def autonomousPeriodic(self) -> None:
        #self.auto.run()
        pass

    def autonomousExit(self) -> None:
        #self.container.drivetrain.resetGyro()
        pass

    def disabledInit(self) -> None:
        pass


if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"

    wpilib.run(Robot)

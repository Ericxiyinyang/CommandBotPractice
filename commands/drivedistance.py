# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.

import commands2

from drivetrain import Drivetrain


class DriveDistance(commands2.CommandBase):
    def __init__(self, speed: float, meters: float, drive: Drivetrain) -> None:
        """Creates a new DriveDistance. This command will drive your robot for a desired distance at
        a desired speed.

        :param speed:  The speed at which the robot will drive
        :param meters: The number of inches the robot will drive
        :param drive:  The drivetrain subsystem on which this command will run
        """
        super().__init__()
        self.distance = meters
        self.fwd_pid
        self.speed = speed
        self.drive = drive
        self.addRequirements([self.drive])

    def initialize(self) -> None:
        """Called when the command is initially scheduled."""
        self.drive.arcadeDrive(0, 0)
        self.drive.resetEncoders()

    def execute(self) -> None:
        """Called every time the scheduler runs while the command is scheduled."""
        self.drive.arcadeDrive(0, self.speed)

    def end(self, interrupted: bool) -> None:
        """Called once the command ends or is interrupted."""
        self.drive.arcadeDrive(0, 0)

    def isFinished(self) -> bool:
        """Returns true when the command should end."""
        # Compare distance travelled from start to desired distance
        return abs(self.drive.averageDistanceMeter()) >= self.distance


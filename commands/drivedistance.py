# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.

import commands2
from superpid import AIOPID
from drivetrain import Drivetrain
from botconstants import RobotConstants as RC


class DriveDistance(commands2.CommandBase):
    def __init__(self, speed: float, dist: float, drive: Drivetrain) -> None:
        super().__init__()
        self.distance = dist
        self.fwd_pid = AIOPID(
            prop=RC.kp,
            integral=RC.ki,
            derivative=RC.kd,
            setPoint=self.distance,
            tol=0.1
        )
        self.rot_pid = AIOPID(
            prop=RC.kpR,
            integral=RC.kiR,
            derivative=RC.kdR,
            setPoint=0.0,
            tol=0.1
        )
        self.drive = drive
        self.addRequirements([self.drive])

    def initialize(self) -> None:
        self.drive.arcadeDrive(0, 0)
        self.drive.resetEncoders()

    def execute(self) -> None:
        self.fwd = self.fwd_pid.calculate(self.drive.averageDistanceMeter())
        self.diff = self.drive.getLEncoderDistance() - self.drive.getREncoderDistance()
        self.rot = self.rot_pid.calculate(self.diff)
        self.drive.arcadeDrive(self.rot, self.fwd)

    def isFinished(self) -> bool:
        return self.fwd_pid.atSetpoint()

    def end(self, interrupted: bool) -> None:
        self.drive.arcadeDrive(0, 0)



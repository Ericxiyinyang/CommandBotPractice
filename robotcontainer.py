import wpilib

#from autoroutine import AutoRoutine
#from drivestraight import DriveStraight
from drivetrain import Drivetrain
from commands.arcadedrive import ArcadeDrive
from commands.drivedistance import DriveDistance
#from gyroturn import GyroTurn
import commands2


class RobotContainer:

    def __init__(self) -> None:
        self.controller = wpilib.Joystick(0)
        # Create SmartDashboard chooser for autonomous routines
        self.chooser = wpilib.SendableChooser()
        self.drivetrain = Drivetrain()
        self._configure()

    def _configure(self):
        # self.chooser.setDefaultOption("Twist 90 degrees", GyroTurn(self.drivetrain, 90))
        # self.chooser.addOption("Go straight 2m", DriveStraight(self.drivetrain, 2))
        # wpilib.SmartDashboard.putData(self.chooser)
        self.chooser.setDefaultOption("Drive 30 cm", DriveDistance(0.5, 0.3, self.drivetrain))
        wpilib.SmartDashboard.putData(self.chooser)
        self.drivetrain.setDefaultCommand(self.getArcadeDriveCommand())



    # def get_autonomous(self) -> AutoRoutine:
    #     return self.chooser.getSelected()

    def getAuto(self) -> commands2.CommandBase:
        return self.chooser.getSelected()

    def getArcadeDriveCommand(self):
        return ArcadeDrive(self.drivetrain, lambda: self.controller.getRawAxis(0), lambda: self.controller.getRawAxis(1))

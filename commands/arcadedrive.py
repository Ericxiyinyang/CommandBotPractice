import commands2
from drivetrain import Drivetrain
import typing

class ArcadeDrive(commands2.CommandBase):
    def __init__(self, drive: Drivetrain,
                 forward: typing.Callable[[], float],
                 rotate: typing.Callable[[], float]):
        super().__init__()
        self.drive = drive
        self.forward = forward
        self.rotate = rotate
        self.addRequirements([self.drive])
        pass

    def initialize(self) -> None:
        pass

    def end(self, interrupted: bool) -> None:
        pass

    def isFinished(self) -> bool:
        return False

    def execute(self) -> None:
        self.drive.arcadeDrive(self.rotate(), self.forward())


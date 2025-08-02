import numpy as np
import numpy.typing as npt
from typing import Optional 
from dataclasses import dataclass 

@dataclass
class FaceAngle:
    pitch: float
    yaw: float
    roll: float

@dataclass
class Person:
    name: str
    face: npt.NDArray[np.float32]





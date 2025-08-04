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
class FaceAuth:
    id: int
    distance: float 

@dataclass
class Face:
    id: int 
    data: npt.NDArray[np.float32]

@dataclass
class Person:
    id: str 
    name: str
    face_id: Optional[int] 
    face: Optional[Face]


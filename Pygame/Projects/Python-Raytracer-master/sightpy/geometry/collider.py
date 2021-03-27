import numpy as np
from ..utils.constants import *
from ..utils.vector3 import vec3
from abc import abstractmethod 

class Collider:    
    def __init__(self,assigned_primitive, center):
        self.assigned_primitive = assigned_primitive
        self.center = center

    @abstractmethod
    def intersect(self, O, D):
        pass
        
    @abstractmethod   
    def get_Normal(self, hit):
        pass
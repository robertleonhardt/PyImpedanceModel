from __future__ import annotations
import numpy as np
import numpy.typing as npt
from .ImpedanceModelElement import ImpedanceModelElement

class G(ImpedanceModelElement):
    """
    (Classical) Gerischer impedance
    
    @version:   AA-20250213
    @author:    Robert Leonhardt <mail@robertleonhardt.de>
    """
    
    # Default min/max values
    _min_value_list: List[float] = [1e-4, 1e-6]
    _max_value_list: List[float] = [1e4, 1e3]
    
    
    def __init__(self, R_Ohm: float = 0.01, tau_s: float = 1):
        """
        Equivalent circuit element: Non-ideal constant phase element
        
        Model function for Gerischer impedance
        Appearance: Asymmetric, non-depressed arc
        Model:      Z = R / sqrt(1 + j * 2 * pi * f * tau)

        Args:
            QR_Ohm (float): Gerischer resistance in Ohm
            tau_s (float): Characteristic time constant in seconds
        """
        self.set_parameters(R_Ohm, tau_s)
        
    
    def evaluate(self, frequency_Hz: npt.ArrayLike) -> npt.ArrayLike:
        return R_Ohm / np.sqrt(1 + 1j * 2 * np.pi * frequency_Hz * tau_s)
    
    
    @property 
    def R_Ohm(self):
        return self._parameter_list[0]
    
    @R_Ohm.setter
    def R_Ohm(self, value):
        self._parameter_list[0] = value
        
    @property 
    def tau_s(self):
        return self._parameter_list[1]
    
    @tau_s.setter
    def tau_s(self, value):
        self._parameter_list[1] = value
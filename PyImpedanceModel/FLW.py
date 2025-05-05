from __future__ import annotations
import numpy as np
import numpy.typing as npt
from .ImpedanceModelElement import ImpedanceModelElement

class FLW(ImpedanceModelElement):
    """
    Equivalent circuit element: Finite-length Warburg impedance
    
    @version:   BA-20250504
                (AA-20221224)
    @author:    Robert Leonhardt <mail@robertleonhardt.de>
    """
    
    # Default min/max values
    _min_value_list: list[float] = [1e-9, 1e-9]
    _max_value_list: list[float] = [1e9, 1e9]
    
    
    def __init__(self, Z_0_Ohm: float = 1e-2, tau_s: float = 1e0):
        """
        Equivalent circuit element: Finite-length Warburg impedance
        
        Short (Finite-Length) Warburg element
        Appearance: Downwards-curled Warburg
        Model:      Z = Z_0_Ohm / sqrt(jw*tau) * tanh(sqrt(jw * tau))

        Args:
            Z_0_Ohm (float): Impedance to which the elements tends for low frequencies
            tau_s (float): Parameter for tuning the frequency behavior
        """
        self.set_parameters(Z_0_Ohm, tau_s)
        
    
    def evaluate(self, frequency_Hz: npt.ArrayLike) -> npt.ArrayLike:
        return self.Z_0_Ohm / np.sqrt(1j * 2 * np.pi * frequency_Hz * self.tau_s) * np.tanh(np.sqrt(1j * 2 * np.pi * frequency_Hz * self.tau_s))
    
    
    @property 
    def Z_0_Ohm(self):
        return self._parameter_list[0]
    
    @Z_0_Ohm.setter
    def Z_0_Ohm(self, value):
        self._parameter_list[0] = value
        
    @property 
    def tau_s(self):
        return self._parameter_list[1]
    
    @tau_s.setter
    def tau_s(self, value):
        self._parameter_list[1] = value
from __future__ import annotations
import numpy as np
import numpy.typing as npt
from .ImpedanceModelElement import ImpedanceModelElement

class R_HN(ImpedanceModelElement):
    """
    Equivalent circuit element: Resistor-HN-parallel element (Havriliak-Negami type)
    
    @version:   AA-20240503
                (AA-20240503)
    @author:    Robert Leonhardt <mail@robertleonhardt.de>
    """
    
    # Default min/max values
    _min_value_list: list[float] = [1e-4, 1e-6, 0, 0]
    _max_value_list: list[float] = [1e4, 1e3, 1, 1]
    
    
    def __init__(self, R_Ohm: float = 0.01, tau_s: float = 1, alpha: float = 0.95, beta: float = 0.95):
        """
        Equivalent circuit element: Resistore-CPE-parallel element
        
        Model function for a parallel connection of a resistor and a CPE with an asymmetric shape
        Appearance: Depressed, asymmetric semi-circle 
        Model:      Z = R / (1 + tau * (jw)^alpha)^beta (Havriliak-Negami element)

        Args:
            R_Ohm (float): Resistance value in Ohm
            tau_s (float): Time constant in Ohm
            alpha (float): Phase angle (0 ... 1) whereas 0 = point (ideal resistor) and 1 = vertical line (ideal capacitor)
            beta (float): Beta parameter (beta = 1 --> Cole Cole)
        """
        self.set_parameters(R_Ohm, tau_s, alpha, beta)
        
    
    def evaluate(self, frequency_Hz: npt.ArrayLike) -> npt.ArrayLike:
        # Calculate equivalent/effective capacitance
        # NOTE: http://www.consultrsr.net/resources/eis/zarc.htm
        return self.R_Ohm / ((1 + (1j * 2 * np.pi * frequency_Hz * self.tau_s) ** self.alpha) ** self.beta)
    
    
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
        
    @property 
    def alpha(self):
        return self._parameter_list[2]
    
    @alpha.setter
    def alpha(self, value):
        self._parameter_list[2] = value
        
    @property 
    def beta(self):
        return self._parameter_list[3]
    
    @beta.setter
    def beta(self, value):
        self._parameter_list[3] = value
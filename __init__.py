# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 11:33:17 2025

@author: Prajwal Anand Muggannavar
"""

"""signal_ICT_StudentName_EnrollmentNo package
Export the three modules: unitary_signals, trigonometric_signals, operations
"""


from .unitary_signals import unit_step, unit_impulse, ramp_signal
from .trigonometric_signals import sine_wave, cosine_wave, exponential_signal
from .operations import time_shift, time_scale, signal_addition, signal_multiplication


__all__ = [
'unit_step', 'unit_impulse', 'ramp_signal',
'sine_wave', 'cosine_wave', 'exponential_signal',
'time_shift', 'time_scale', 'signal_addition', 'signal_multiplication'
]
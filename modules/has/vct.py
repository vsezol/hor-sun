import numpy as np
import math

class HorSunVct:
    """
        решает систему уравнений и находит коэффициенты k и b
    """
    @staticmethod
    def get_linear_eq(x1, y1, x2, y2):
        M = np.array([[x1, 1.], [x2, 1.]])
        v = np.array([y1, y2])
        k, b = np.linalg.solve(M, v)
        return k, b
import pytest
import numpy
import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

import src.BMI.BMICalc as BMI
import src.Webapp.app as Webapp

# Webapp.createApp()


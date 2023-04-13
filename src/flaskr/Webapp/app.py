from flask import Flask

import pytest
import numpy
import sys
from pathlib import Path

path_root = Path(__file__).parents[3]
sys.path.append(str(path_root))

import src.BMI.BMICalc as BMI
import src.flaskr.Webapp.app as Webapp
from src.flaskr import create_app

# Webapp.createApp()
app = create_app()
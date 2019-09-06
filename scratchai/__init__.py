import os
if 'DISPLAY' not in os.environ:
  import matplotlib as mpl
  mpl.use('Agg')

from scratchai import datasets
from scratchai import attacks
from scratchai import DataLoader
from scratchai import utils
from scratchai import nets
from scratchai import init
from scratchai import pretrained
from scratchai import imgutils
from scratchai import one_call
from scratchai import trainers
from scratchai._config import *

import os
import logging as LOG

# TODO Confirm if this is the most efficient way to do so.
if not os.path.exists(home):
  os.makedirs(home)

# Setting Logging to DEBUG Level
LOG.basicConfig(level=LOG.DEBUG)

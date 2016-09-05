import numpy as np
import scipy as sp
import numpy.random
import scipy.linalg as sla
import numpy.linalg as nla
import scipy.stats as ss
import sys
import os.path
import importlib

assert sys.version_info >= (3,5)

import matplotlib
#matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
#plt.switch_backend('Qt4Agg')
plt.ion()
from mpl_toolkits.mplot3d import Axes3D

# With Qt4Agg backend plt.pause() causes warning. Ignore.
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

from numpy import sqrt, abs, floor, ceil, prod, \
    mean, \
    linspace, arange, reshape, \
    pi, log, sin, cos, tan, \
    array, asarray, matrix, asmatrix, \
    eye, zeros, ones, diag, \
    trace, \
    dot

from scipy.linalg import sqrtm, inv, eigh, svd

np.set_printoptions(precision=5)
np.set_printoptions(suppress=True)
# Only applies to arrays. I.e. we will still
# get full precision by inspecting individual elements

from time import sleep


######################
# From DAPPER
######################

from aux.stoch import *
from aux.utils import *
from aux.misc import *
from aux.series import *
from stats import *
from aux.viz import *
from aux.chronos import *
from aux.matrices import *
from aux.randvars import *
from da_algos import *
from aux.admin import *


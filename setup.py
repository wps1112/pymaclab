#!/usr/bin/env python

from datetime import datetime

# import setuptools # have to do this to be able to setup.py develop
from numpy.distutils.core import setup
from numpy import get_include

DESCRIPTION="The Python Macroeconomics Library"
LONG_DESCRIPTION="""
PyMacLab stands for Python Macroeconomics Library which currently primarily serves the purposes of providing
a convenience framework written in Python to solve non-linear DSGE models. At the time of writing this the library
supports solving DSGE models using 1st and 2nd order perturbation methods which are computed around the steady state.
In particular, the library provides wrapper function for [Paul Klein's](http://paulklein.ca/newsite/start/start.php)
1st-order accurate method based on the Schur Decomposition as well a more recently published method by the same author
(co-authored with Paul Gomme, see [here](http://ideas.repec.org/a/eee/dyncon/v35y2011i4p604-615.html)) which provides
2nd-order accurate solutions without using Tensor Algebra (using the Magnus and Neudecker 1999 definition of the
Hessian matrix).

The library is extremely user-friendly in the sense of employing a model text file parser similar to that present in
[Dynare](http://www.dynare.org/) which requires users to only write down the original set of non-linear first-order
conditions of optimality. In addition, users are offered a menu of options of how to provide information required for
calculating the steady state of the model. Once the model is parsed and read in, several options of solving it exist
and users are provided with further convenience methods suitable for simulating solved models and investigating dynamic
statistical properties.

It should also be mentioned that because PyMacLab is a convenience library of highly modular nature (using
a object-oriented programming approach) it is very easy to loop over one model several thousand times each time changing
the original set of primitive parameters, such as depreciation rates, impatience factors, etc. in order to compute
solutions of the same model over a large set of conceivable parameterisations. Also, whenever solution methods require
the calculation of the Jacobian or Hessian, this is always done analytically (symbolically) using the Python
symbolic computation library [SympyCore](http://code.google.com/p/sympycore/) and not numerically as in other software
packages. Sympycore is not supplanted by Sympy, but it works well at the moment so we will alter PyMacLab at a later
stage to reflect this.

PyMacLab was authored by [Eric M. Scheffel](http://www.ericscheffel.com) who is currently working as [Assistant Professor
in Economics at Nottingham University China](http://www.nottingham.edu.cn/en/business/people/staffprofile/eric-scheffel.aspx)
and is distributed under the GNU General Public License v3.0.
"""

DISTNAME = 'pymaclab'
LICENSE ="""
Copyright 2007-2012 Eric M. Scheffel

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
AUTHOR = "Eric M. Scheffel"
MAINTAINER = "Eric M. Scheffel"
MAINTAINER_EMAIL = "emscheffel@gmail.com"
URL = 'http://github.com/escheffel/pymaclab/'
DOWNLOAD_URL="http://github.com/escheffel/pymaclab/tarball/v0.85"
CLASSIFIERS=["Scientific", "Macroeconomics", "General Equilibrium", "DSGE", "Time Series"]

MAJOR = 0
MINOR = 85
MICRO = 0
ISRELEASED = True
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)
FULLVERSION = VERSION
if not ISRELEASED:
    FULLVERSION += '.dev'

def write_version_py(filename='./version.py'):
    cnt = """\
from datetime import datetime

version = '%s'
"""
    a = open(filename, 'w')
    try:
        a.write(cnt % FULLVERSION)
    finally:
        a.close()

def configuration(parent_package='', top_path=None, package_name=DISTNAME):
#    write_version_py()

    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path,
                           version=FULLVERSION)
    config.set_options(ignore_setup_xxx_py=True,
                       assume_default_configuration=True,
                       delegate_options_to_subpackages=True,
                       quiet=True)

    config.add_subpackage('pymaclab')
    return config

if __name__ == '__main__':
    setup(name=DISTNAME,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          license=LICENSE,
          url=URL,
          download_url=DOWNLOAD_URL,
          long_description=LONG_DESCRIPTION,
          classifiers=CLASSIFIERS,
          platforms='any',
          configuration=configuration)

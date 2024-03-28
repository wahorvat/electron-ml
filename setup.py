"""Setup for pip package."""

import unittest

from setuptools import find_packages
from setuptools import setup

with open(r'README.md', mode=r'r') as readme_handle:
    long_description = readme_handle.read()


REQUIRED_PACKAGES = [
    'absl-py',
    'attrs',
    'chex',
    'h5py',
    'folx @ git+https://github.com/microsoft/folx',
    'jax',
    'jaxlib',
    'kfac_jax @ git+https://github.com/deepmind/kfac-jax',
    'ml-collections',
    'optax',
    'numpy',
    'pandas',
    'pyscf',
    'pyblock',
    'scipy',
    'tables',
    'typing_extensions',
    'sympy',
    'opt_einsum_fx>=0.1.4',
]



def ferminet_test_suite():
  test_loader = unittest.TestLoader()
  test_suite = test_loader.discover('ferminet/tests', pattern='*_test.py')
  return test_suite

setup(
    name=r'hopfield-electrons',
    version=r'0.1',
    author=r'William Horvat',
    author_email=r'horvat@gmail.com',
    url=r'https://github.com/ml-jku/hopfield-layers',
    description=r'Quantum Wavefunctionn Approximation with Continuous Hopfield Layers and Equivariant Layers',
    long_description=long_description,
    long_description_content_type=r'text/markdown',
    scripts=['bin/ferminet'],
    packages=find_packages(),
    python_requires=r'>=3.8.0',
    install_requires=REQUIRED_PACKAGES,
    test_suite='setup.ferminet_test_suite',
)

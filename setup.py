import setuptools

with open(r'README.md', mode=r'r') as readme_handle:
    long_description = readme_handle.read()

setuptools.setup(
    name=r'hopfield-electrons',
    version=r'0.1',
    author=r'William Horvat',
    author_email=r'horvat@gmail.com',
    url=r'https://github.com/ml-jku/hopfield-layers',
    description=r'Quantum Wavefunctionn Approximation with Continuous Hopfield Layers and Equivariant Layers',
    long_description=long_description,
    long_description_content_type=r'text/markdown',
    packages=setuptools.find_packages(),
    python_requires=r'>=3.8.0',
    install_requires=[
        r'torch>=1.8.0',
        r'numpy>=1.20.0'
        r'sympy',
        r'scipy',
        r'opt_einsum_fx>=0.1.4'
    ],
    zip_safe=True
)

from setuptools import setup, find_packages

setup(
    name='PLSP',
    version=1.0,
    license='MIT',
    maintainer='Neon K.I.D<Kwang Soo Jeong>',
    maintainer_email='contact@neonkid.xyz',
    description='Large size Pathology Image Processing Module',
    keywords=['Pathology Image', 'SVS', 'PLSP', 'Large-size'],
    url='https://github.com/NEONKID/PLSP',
    install_requires=[
        'openslide-python',
        'numpy',
        'pyvips',
        'czifile'
    ],
    packages=find_packages(),
    python_requires = '>=3.5',
    zip_safe=False
)
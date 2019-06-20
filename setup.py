from setuptools import setup

setup(
    name='PLSP',
    version=1.0,
    maintainer='Neon K.I.D<Kwang Soo Jeong>',
    maintainer_email='contact@neonkid.xyz',
    description='Large size Pathology Image Processing Module',
    keywords=['Pathology Image', 'SVS', 'CZI', 'Large-size'],
    url='https://github.com/NEONKID/PILP',
    install_requires=[
        'openslide-python',
        'numpy',
        'pyvips',
        'czifile'
    ],
    zip_safe=True
)
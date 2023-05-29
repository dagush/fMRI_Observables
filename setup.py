'''setup.py'''

from setuptools import setup, find_packages


with open("requirements.txt") as reqs_file:
    REQS = [line.rstrip() for line in reqs_file.readlines() if line[0] not in ['\n', '-', '#']]

setup(
    name =  'fMRI-Observables',
    description = 'A package to compute fMRI-based observables.',
    url =  'https://github.com/dagush/fMRI_Observables',
    version =  '1.0.0',
    license =  'Apache License 2.0',

    author =  'Gustavo Patow',
    author_email =  'gustavo.patow@udg.edu',

    install_requires =  REQS,
    packages =  find_packages(exclude=['doc', '*tests*']),
    scripts =  [],
    include_package_data =  True,

    keywords =  'fMRI, Obervables, FC, FCD',
    classifiers =  [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

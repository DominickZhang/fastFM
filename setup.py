from setuptools import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

ext_modules = [
    Extension('ffm', ['fastFM2/ffm.pyx'],
              libraries=['m', 'fastfm'],
              library_dirs=['fastFM2/', 'fastFM-core/bin/'],
              include_dirs=['fastFM2/', 'fastFM-core/include/',
                            'fastFM-core/externals/CXSparse/Include/',
              numpy.get_include()])]

setup(
    name='fastFM2',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules,

    packages=['fastFM2'],

    package_data={'fastFM2': ['fastFM2/*.pxd']},

    version='0.3.1',
    url='https://github.com/DominickZhang/fastFM',
    author='Jinnian Zhang',
    author_email='jinnian.zhang@wisc.edu',

    # Choose your license
    license='BSD',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',

        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['numpy', 'scikit-learn', 'scipy', 'cython']
)

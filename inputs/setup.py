from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('track_line_filter.pyx'), requires=['numpy', 'cv2', 'matplotlib', 'scipy', 'getch',
                                                                'board'])

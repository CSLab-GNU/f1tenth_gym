from setuptools import setup

setup(name='f110_gym',
      version='0.2.1',
      author='Hongrui Zheng',
      author_email='billyzheng.bz@gmail.com',
      url='https://f1tenth.org',
      install_requires=['gym==0.19.0',
                        'numpy==1.20.0',
                        'Pillow>=8.3.2',
                        'scipy==1.7.3',
                        'numba',
                        'pyyaml>=5.4',
                        'pyglet',
                        'pyopengl']
      )

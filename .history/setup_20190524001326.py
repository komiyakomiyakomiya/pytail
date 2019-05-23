from setuptools import setup, find_packages

setup(
    name='wonder_tool',
    version='1.0',
    packages=find_packages(),
    install_requires=['cliff'],
    entry_points={
        'console_scripts':
            'tail = 'tail_command_by_python.main:tail_main'
    },
    zip_safe=False,
    classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
    ],
)
from setuptools import setup, find_packages

setup(
    name='tail_command_by_python',
    version='1.0',
    packages=find_packages(),
    install_requires=['cliff'],
    entry_points={
        'console_scripts':
            'pytail = tail_command_by_python.main:tail_main'
    },
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7.3',
    ],
)

from setuptools import setup

setup(
    name='roboclaw',
    version='1.0.0.dev1',
    packages=['roboclaw'],
    url='https://github.com/urill/pyroboclaw',
    license='MIT',
    author='Keshuai Xu and Ben Gillette',
    author_email='urillx@gmail.com',
    description='Unofficial python library for talking to RoboClaw motor controllers',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='pololu roboclaw motor',
    install_requires=['pyserial', 'pycrc'],

)

from setuptools import setup, find_packages
import tweethread

INSTALL_REQUIRES = [
    'tweepy', 'nltk'
]

setup(
    name='tweethread',
    version=tweethread.__version__,
    description=tweethread.__doc__.strip(),
    download_url='https://github.com/rcurtiss/tweethread',
    author=tweethread.__author__,
    author_email='rcurtiss@gmail.com',
    license=tweethread.__license__,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tweethread = tweethread.__main__:main'
        ]
    },
    install_requires=INSTALL_REQUIRES
)

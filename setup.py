from distutils.core import setup
import posixtools

setup(
    name=posixtools.__title__,
    version=posixtools.__version__,
    author=posixtools.__author__,
    author_email='chywoo@gmail.com',
    url='http://',
    packages=[posixtools.__title__],
    package_dir={posixtools.__title__:posixtools.__title__},
    license='BSD New',
    zip_safe=True,
    classifiers=(
        # 'Development Status :: 5 - Production/Unstable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD new',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ),
    description = 'PosiX Tools for Python', requires=['psutil']
    )
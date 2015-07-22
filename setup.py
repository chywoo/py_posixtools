from distutils.core import setup
import pxt

setup(
    name=pxt.__title__,
    version=pxt.__version__,
    author=pxt.__author__,
    author_email='chywoo@gmail.com',
    url='http://',
    packages=[pxt.__title__],
    package_dir={pxt.__title__:pxt.__title__},
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
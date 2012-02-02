try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

install_requires = [
    'Django',
]

setup(
    name='django-ajaxutils',
    version="0.1.0",
    description='Ajax requests for Ponies',
    url='http://github.com/ahref/django-ajaxutils',
    packages=['ajaxutils'],
    zip_safe=True,
    license='BSD',
    classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
    install_requires=install_requires,
)
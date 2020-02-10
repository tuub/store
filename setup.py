from setuptools import setup, find_packages

setup(
    name = 'store',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = [
        "Flask==1.1.1",
        "Flask-Login==0.4.1",
        "Flask-WTF==0.14.2",
        "Werkzeug==0.16.0",
        "requests"
    ],
    url = 'http://cottagelabs.com/',
    author = 'Cottage Labs',
    author_email = 'us@cottagelabs.com',
    description = 'Provision of a web API wrapper for storage system',
    license = 'MIT',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Copyheart',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)

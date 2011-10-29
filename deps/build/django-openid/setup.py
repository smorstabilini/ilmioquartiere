from setuptools import setup, find_packages

setup(
    name='django-openid',
    version='0.2.0',
    description='OpenID tools for Django',
    author='Simon Willison',
    author_email='simon@simonwillison.net',
    url='http://code.google.com/p/django-openid/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    package_data = {
        'django_openid': [
            'docs/intro.txt',
            'templates/django_openid/*.html'
        ],
        'django_openidconsumer': [
            'templates/*.html',
        ]
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=['python-openid'],
)

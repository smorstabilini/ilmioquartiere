from distutils.core import setup
 
setup(
    name='django-gravatar',
    version='0.1.0',
    description='Gravatar Support in a Django Reusable Application',
    author='James Tauber',
    author_email='jtauber@jtauber.com',
    url='http://django-gravatar.googlecode.com',
    packages=[
        'gravatar',
        'gravatar.templatetags',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
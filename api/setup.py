from setuptools import setup

setup(
    name='bora_app',
    packages=['bora_app_pkg'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-cors'
        'pyjwt',
        'pymongo',
        'pymongo[srv]',
        'mongoengine',
        'python-dotenv'
    ],
)

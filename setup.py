# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='flask-neomodel',
    version='0.1',
    description='Flask extension for OGM on neo4j python driver',
    author="Paolo D'Onorio De Meo",
    author_email='p.donorio.de.meo@gmail.com',
    # url='',
    license='MIT',
    packages=['.'],
    # package_data={
    #     main_package: [
    #         'logging.ini',
    #         'logging_tests.ini'
    #     ]
    # },
    python_requires='>=3.4',
    install_requires=[
        'flask',    # 1.0.2
        'neomodel'  # 3.2.8
    ],
    classifiers=[
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=['flask', 'neo4j', 'models', 'neomodel']
)

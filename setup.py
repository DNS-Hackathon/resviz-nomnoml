from setuptools import find_packages, setup

setup(
    name='resviz',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.8.0',
    install_requires=[
        'flask',
    ],
    extras_require={
    },
    entry_points={
    },
    scripts=[
    ],
)

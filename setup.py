import setuptools

setuptools.setup(
    name="awarc-master",
    version="0.0.3",
    author="17876",
    author_email="17876@protonmail.com",
    description="tools for working with file archive",
    url="https://github.com/17876/awarc.git",
    py_modules=["arc"],
    install_requires=['setuptools==49.2.0'
                      ],
    packages=setuptools.find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X"
    ]
)

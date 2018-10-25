import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stock_notifier",
    version="0.0.1",
    author="Saswat Raj",
    author_email="saswatraj@outlook.com",
    description="An application that provides system notifications for changes in stock values",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Environment :: MacOS X",
    ],
    entry_points = {
        'console_scripts': [
            'stock-notify=stock_notifier.command_line:main'
        ]
    }
)

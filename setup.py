from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="noscrape",  # Replace with your own package name
    version="1.0.0",  # Initial release version
    author="Bernhard Schönberger",
    author_email="noscrape@gmx.de",
    description="A package to obfuscate text using Unicode Private Use Area characters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/noscrape/noscrape-python",  # Replace with the URL of your project
    packages=find_packages(),  # Automatically find and include all packages in the project
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the Python versions compatible with your package
    install_requires=[
        # List your package dependencies here
        # e.g., 'requests', 'numpy',
    ],
    entry_points={
        'console_scripts': [
            'noscrape=noscrape.__main__:main',  # Replace with the entry point for your package
        ],
    },
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
)

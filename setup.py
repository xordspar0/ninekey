import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ninekey",
    version="0.2.0",
    author="Jordan Christiansen",
    author_email="xordspar0@gmail.com",
    description="A barebones hotkey/launcher application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xordspar0/ninekey",
    packages=setuptools.find_packages(),
    test_suite="ninekey",
    install_requires=[
        "PyQt5",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)

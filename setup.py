import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="exception_decorator",
    version="0.0.1",
    author="Mauricio Zambrano",
    author_email="mzambran@gmail.com",
    description="An extensible decorator to catch any python error on file, mail, queue...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved ::  GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "exception_decorator"},
    packages=setuptools.find_packages(where="exception_decorator"),
    python_requires=">=3.6",
)

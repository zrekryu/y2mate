from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name="y2mate",
    version="1.0.0",
    description="An unofficial API wrapper for Y2Mate.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Zrekryu",
    author_email="zrekryu@gmail.com",
    url="https://github.com/zrekryu/y2mate-api",
    keywords=["y2mate", "y2mate-api", "youtube"]
    packages=find_packages(),
    install_requires=[
        "http"
        ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.x",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities",
        ]
    )
"""Setup script for calculator package."""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="calculator",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A professional Python calculator with comprehensive testing and documentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/calculator",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/calculator/issues",
        "Documentation": "https://github.com/yourusername/calculator/blob/main/docs/README.md",
        "Source Code": "https://github.com/yourusername/calculator",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "flake8>=6.1.0",
            "mypy>=1.5.0",
            "pre-commit>=3.3.0",
        ],
    },
    package_data={
        "calculator": ["py.typed"],
    },
    include_package_data=True,
)

# Made with Bob

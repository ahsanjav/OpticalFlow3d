from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name='opticalflow3d',
    version="0.3.2",
    description='GPU/CUDA optimized implementation of 3D optical flow algorithms such as Farneback and Lucas-Kanade',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        "numpy>=1.24.4",
        "numba>=0.61.2",
        "scikit-image>=0.18.0",
        "scipy>=1.1.0",
        "tqdm>=4.62.0",
        "cupy-cuda12x>=10.0.0"
    ],
    author='Xianbin Yong',
    author_email='xianbin.yong13@sps.nus.edu.sg',
    url='https://gitlab.com/xianbin.yong13/opticalflow3d',
    packages=find_packages(),
    python_requires='>=3.7',
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Topic :: Scientific/Engineering",
    ],
)

import setuptools

with open("README.md", mode="r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRED_PACKAGES = [
    'hangul_utils'
]

setuptools.setup(
    name="ko_noiser",
    version="0.2.3",
    author="David Moedinger",
    author_email="david.moedinger@ketzu.net",
    description="ko_noiser: Synthetic Sentence Noise Generator for Korean",
    install_requires=REQUIRED_PACKAGES,
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ketzu/konoise",
    packages=setuptools.find_packages(),
    package_data={'ko_noiser': ['ko_noiser/idioms.csv']},
    python_requires=">=3.7",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)

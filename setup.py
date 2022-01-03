import setuptools

with open("README.md", mode="r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRED_PACKAGES = [
    'hangul_utils',
    #'git+https://github.com/ketzu/g2pk.git'
    # 'g2pK' not sure how to handle alternative g2pK-kiwipiepy as I haven't published it
    # but 'g2pK would work as well
]

setuptools.setup(
    name="ko_noiser",
    version="0.1.2",
    author="David Moedinger",
    author_email="david.moedinger@ketzu.net",
    description="ko_noiser: Synthetic Sentence Noise Generator for Korean",
    install_requires=REQUIRED_PACKAGES,
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ketzu/konoise",
    packages=setuptools.find_packages(),
    package_data={'konoise': []},
    python_requires=">=3.6",
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)

#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="ncbi-refseq-accession-offsets",
    version="2021.3.25",
    url="https://github.com/chanzuckerberg/taxoniq",
    license="MIT License",
    author="Andrey Kislyuk",
    author_email="akislyuk@chanzuckerberg.com",
    description="Taxoniq accession index for NCBI BLAST databases",
    long_description="Taxoniq accession index for NCBI BLAST databases",
    packages=find_packages(),
    include_package_data=True
)

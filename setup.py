from setuptools import setup

version = '1.0.0'

setup(
    name = 'decoypyrat',
    version = version,
    packages = ['decoypyrat'],
    description = 'Fast Hybrid Decoy Sequence Database Creation for Proteomic Mass Spectrometery Analyses',
    author = 'James Wright',
    author_email = 'james.wright@sanger.ac.uk',
    url = 'https://github.com/wtsi-proteomics/DecoyPYrat',
    keywords = ['database searching',' fdr',' python',' sequence database',' shotgun proteomics',' target-decoy'],
    install_requires=[
    ],
    license = 'MIT',
    entry_points={
        'console_scripts': [
            'decoypyrat = decoypyrat.decoyPYrat:main'
        ]
    }
)

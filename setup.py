import setuptools


def main():
    with open('README.md', 'r') as fp:
        readme = fp.read()

    setuptools.setup(
        name='combination_py',
        version='1.0.0',
        description='Python package for combination calculation',
        long_description=readme,
        long_description_type='text/markdown',
        url='https://github.com/m-star18/combination_py',
        license='Apache Software License 2.0',
        author='m_star18',
        author_email='31807@toyota.kosen-ac.jp',
        packages=['combination'],
    )

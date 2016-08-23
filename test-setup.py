from setuptools import setup

setup(
    name="slack-lambda",
    version="0.0.1",
    author="unfoldingWord",
    author_email="unfoldingword.org",
    description="Unit test setup file.",
    license="MIT",
    keywords="",
    url="https://github.org/unfoldingWord-dev/slack-lambda",
    long_description='Unit test setup file',
    classifiers=[],
    install_requires=[
        'requests',
        'pyaes'
    ],
    test_suite='tests'
)

from setuptools import setup, find_packages

setup(
    name='skygrid-docker-worker',
    version='0.5.6',
    url='https://github.com/skygrid/docker-worker',
    author='Alexander Baranov',
    author_email='sashab1@yandex-team.ru',
    packages=find_packages(),
    description='SkyGrid docker worker',
    install_requires=[
        "lockfile",
        "requests>=2.5.1",
        # TODO: error? docker.errors.InvalidVersion: API versions below 1.21
        # are no longer supported by this library.
        "docker-py>=1.1.0",
        "six==1.9.0",
        "raven",
        "hep-data-backends",
        "marshmallow",
        "wonderlandClient",
        "protobuf",
    ],
    scripts=[
        'scripts/test-descriptor'
    ]
)

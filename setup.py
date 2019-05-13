import setuptools

setuptools.setup(
    name="futurewater-djangoapp",
    version="0.0.1",
    description="Futurewater plugin to Airavata Django Portal",
    packages=setuptools.find_packages(),
    install_requires=[
        'django>=1.11.16',
    ],
    entry_points="""
[airavata.djangoapp]
futurewater = futurewater.apps:FuturewaterConfig
""",
)

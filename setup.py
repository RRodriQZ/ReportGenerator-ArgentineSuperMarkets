from setuptools import setup


dependencies = [
    "beautifulsoup4==4.9.3",
    "marshmallow==3.13.0",
    "requests==2.25.0",
    "urllib3==1.26.6",
]

package_data = {
    "mail.resources": ["config.ini"],
}

packages = [
    "controller",
    "functions",
    "log",
    "mail",
    "mail.resources",
    "model",
    "schemas",
    "scrap",
    "view",
]

platform = ["any"]

long_description = "Report product prices from argentine supermarkets"

manifest = dict(
    name="report-ArgentineSuperMarkets",
    version="1.0.0",
    author="DobleRR - Rodrigo Quispe",
    author_email="rrquispezabala@gmail.com",
    description="Report from Argentine SuperMarkets prices",
    url="https://github.com/RRodriQZ",
    license="MIT",
    python_requires=">=3.6, <4",
    keywords="Dia SuperMarket Argentine",
    install_requires=dependencies,
    package_data=package_data,
    packages=packages,
    platforms=platform,
    long_description=long_description,
    long_description_content_type="text/markdown",
)


if __name__ == "__main__":
    setup(**manifest)

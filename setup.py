from setuptools import setup

setup(
    name="briefme-test-user",
    version="0.1",
    description="Model user for testing purposes",
    url="https://github.com/briefmnews/briefme-test-user",
    author="Brief.me",
    author_email="tech@brief.me",
    packages=[
        "briefme_test_user",
        "briefme_test_user.migrations",
    ],
    python_requires=">=3.7",
    install_requires=["Django>=2.2"],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
    zip_safe=False,
)

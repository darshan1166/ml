from setuptools import setup,find_packages

def install_requires(path) :
    HYPEN_E_DOT = '-e .'
    requirements = []
    with open(path) as file:
        requirements = file.readlines()
        requirements = [req.replace("/n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='ml',
    packages=find_packages(),
    install_requires=install_requires("requirements.txt")
)
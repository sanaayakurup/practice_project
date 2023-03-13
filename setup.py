from setuptools import find_packages,setup #will find all the packages 
#https://www.youtube.com/watch?v=Rv6UFGNmNZg
def get_requirements(file_path):
    ''' 
    This func returns a list of required pacakges
    '''
    requirements=[]
    hyphene="-e ."
    with open(file_path,'r') as file:
        requirements=file.readlines()
        requirements=[r.replace("\n","") for r in requirements]

        if hyphene in requirements:
            requirements.remove(hyphene)
    return requirements


setup(
name='mlproject'
,version='0.0.1'
,author='sanaaya'
,author_email='sanaaya.kurup@gmail.com'
,packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
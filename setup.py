from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='cluster_manager',
      version='0.1',
      description='Distributes jobs across a number of remote workers via SSH',
      long_description='Given data about workers (IP, access credentials, no. of CPUs etc.) and a list of jobs, '
                       'distributes the computing load across the workers. Supports upload of necessary file and'
                       'download of output files for each job.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Distributed Computing',
        'Intended Audience :: Science/Research'
      ],
      keywords='cluster distributed ssh',
      url='https://github.com/nazgul17/cluster_manager',
      author='Marco Tamassia',
      author_email='marco.tamassia@protonmail.com',
      license='MIT',
      packages=['cluster_manager'],
      install_requires=[
          'joblib',
          'paramiko',
          'future'
      ],
      include_package_data=True,
      zip_safe=False)

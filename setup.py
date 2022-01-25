from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='charcade',
  version='1.0.2',
  description='String manipulation.',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
  long_description_content_type='text/markdown',
  url='',  
  author='Aaron Clayton',
  author_email='ecoahaaron@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='string', 
  packages=find_packages(),
  package_data={
    'charcade': ['charcade/words_by_letter/*.txt']
  },
  include_package_data=True,
  zip_safe=False,
  install_requires=['']
)


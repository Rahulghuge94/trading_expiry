import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name = "trading_expiry",
    version = "0.1",
    packages=setuptools.find_packages(),
    version = '0.2',
    include_package_data=True,
    description = 'finvasia unofficial Trading api',
    long_description=long_description,
    long_description_content_type="text/markdown",  author = 'Rahul',
    author_email = '1994ghuge.gmail.com',
    url = 'https://github.com/Rahulghuge94/finshoonya',
    install_requires=['requests', 'pandas','pytz','websocket-client'],
    keywords = ['NSE', 'OPTION', 'FUTURE' 'python', 'sdk', 'trading', 'stock markets'],
    classifiers=[
      'Intended Audience :: Developers',
      'Natural Language :: English',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3.6'])

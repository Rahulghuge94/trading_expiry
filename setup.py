import setuptools

setuptools.setup(
    name = "trading_expiry",
    version = "0.1",
    packages=setuptools.find_packages(),
    include_package_data=True,
    description = 'library to get trading expiries.',
    long_description="library to get trading expiries.",
    long_description_content_type="text/markdown",  author = 'Rahul',
    author_email = '1994ghuge.gmail.com',
    url = 'https://github.com/Rahulghuge94/trading_expiry',
    install_requires=['requests', 'datetime','json'],
    keywords = ['NSE', 'OPTION', 'FUTURE' 'python', 'sdk', 'trading', 'stock markets'],
    classifiers=[
      'Intended Audience :: Developers',
      'Natural Language :: English',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3.6'])

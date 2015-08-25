# linkchecker-tryer
A wrapper for linkchecker to retry failed links.

## Installation
You need to install linkchecker first:
https://github.com/wummel/linkchecker

Linkchecker-tryer hasn't registered in Pypi yet. So you need

  [sudo] python setup.py install
  
## Usage

  linkchecker --check-extern http://my.link | linkchecker-tryer

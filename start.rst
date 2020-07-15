.. hello-rest documentation master file, created by
   sphinx-quickstart on Wed Jul 15 16:01:58 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

RestructedText 시작하기
=======================

1. 스핑크스 파이썬 패키지를 설치한다.

``$ pip install sphinx sphinx_theme``

2. 스핑크스 템플릿을 생성한다.

``$ sphinx-quickstart``

|   Welcome to the Sphinx 1.5.4 quickstart utility.
|
|   Please enter values for the following settings (just press Enter to
|   accept a default value, if one is given in brackets).
|
|   Enter the root path for documentation.
|   > Root path for the documentation [.]:
|
|   You have two options for placing the build directory for Sphinx output.
|   Either, you use a directory "_build" within the root path, or you separate
|   "source" and "build" directories within the root path.
|   > Separate source and build directories (y/n) [n]:
|
|   Inside the root directory, two more directories will be created; "_templates"
|   for custom HTML templates and "_static" for custom stylesheets and other static
|   files. You can enter another prefix (such as ".") to replace the underscore.
|   > Name prefix for templates and static dir [_]:
|
|   The project name will occur in several places in the built documentation.
|   > Project name: hello-rest
|   > Author name(s): user
|
|   Sphinx has the notion of a "version" and a "release" for the
|   software. Each version can have multiple releases. For example, for
|   Python the version is something like 2.5 or 3.0, while the release is
|   something like 2.5.1 or 3.0a1.  If you don't need this dual structure,
|   just set both to the same value.
|   > Project release []: 3.5
|
|   If the documents are to be written in a language other than English,
|   you can select a language here by its language code. Sphinx will then
|   translate text that it generates into that language.
|
|   For a list of supported codes, see
|   http://sphinx-doc.org/config.html#confval-language.
|   > Project language [en]: ko
|
|   The file name suffix for source files. Commonly, this is either ".txt"
|   or ".rst".  Only files with this suffix are considered documents.
|   > Source file suffix [.rst]:
|
|   One document is special in that it is considered the top node of the
|   "contents tree", that is, it is the root of the hierarchical structure
|   of the documents. Normally, this is "index", but if your "index"
|   document is a custom template, you can also set this to another filename.
|   > Name of your master document (without suffix) [index]:
|
|   Sphinx can also add configuration for epub output:
|   > Do you want to use the epub builder (y/n) [n]:
|
|   Please indicate if you want to use one of the following Sphinx extensions:
|   > autodoc: automatically insert docstrings from modules (y/n) [n]: y
|   > doctest: automatically test code snippets in doctest blocks (y/n) [n]: y
|   > intersphinx: link between Sphinx documentation of different projects (y/n) [n]:
|   > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y
|   > coverage: checks for documentation coverage (y/n) [n]: y
|   > imgmath: include math, rendered as PNG or SVG images (y/n) [n]: n
|   > mathjax: include math, rendered in the browser by MathJax (y/n) [n]: y
|   > ifconfig: conditional inclusion of content based on config values (y/n) [n]: y
|   > viewcode: include links to the source code of documented Python objects (y/n) [n]: y
|   > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: y
|
|   A Makefile and a Windows command file can be generated for you so that you
|   only have to run e.g. 'make html' instead of invoking sphinx-build
|   directly.
|   > Create Makefile? (y/n) [y]:
|   > Create Windows command file? (y/n) [y]:
|
|   Creating file .\conf.py.
|   Creating file .\index.rst.
|   Creating file .\Makefile.
|   Creating file .\make.bat.
|
|   Finished: An initial directory structure has been created.
|
|   You should now populate your master file .\index.rst and create other documentation
|   source files. Use the Makefile to build the docs, like so:
|      make builder
|   where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

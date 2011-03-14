from setuptools import setup, find_packages

setup( name = "MylittleCrawler",
version = "0.1", packages = find_packages(), scripts = ["mycrawler"],
install_requires = ["BeautifulSoup"], package_data = {"pymycrawler": ['']},
author = "me", author_email="me@yo.es",description="yo molo",license="MIT",
keywords= "",url=" ",long_description="yo molo mas",download_url="")

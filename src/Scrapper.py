from bs4 import BeautifulSoup
import requests


class Scrapper:
    """ Class to retrieve all the data of a site in a more or less targeted way """

    def __init__(self, url):
        """ Class builder """

        self.url = url
        self.soup = BeautifulSoup(requests.get(self.url).text, 'html.parser')  # Content of the html page

    def get_soup(self):
        """ Retrieve all content of the html page """

        return self.soup

    def get_specific_div_of_soup(self, div):
        """ Retrieve specific div of the html page """

        content_list = self.soup.find_all(div)
        return [content.text for content in content_list]

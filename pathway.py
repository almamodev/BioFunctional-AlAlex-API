import bs4
import requests
import typing


class Pathway:
    @classmethod
    def response(cls) -> str:
        URL: str = 'https://www.kegg.jp/kegg/pathway.html'

        response: requests.Response = requests.get(URL)
        response.raise_for_status()

        return response.text
        

    @classmethod
    def beautiful_soup(cls) -> bs4.BeautifulSoup:
        markup: str = cls.response()
        features: str = 'html.parser'

        return bs4.BeautifulSoup(markup, features)
    

    @classmethod
    def interactions(cls) -> typing.List[str]:
        beautiful_soup: bs4.BeautifulSoup = cls.beautiful_soup()

        interactions: typing.List = []

        for h4 in beautiful_soup.find_all('h4', attrs={'id': True}):
            interaction: str = h4.text.split('.')[0]
            interactions.append(interaction)

        return interactions
    

    @classmethod
    def reactions(cls) -> typing.List[str]:
        beautiful_soup: bs4.BeautifulSoup = cls.beautiful_soup()

        reactions: typing.List = []

        for b in beautiful_soup.find_all('b')[8:]:
            reaction: str = b.text.split()[0]
            reactions.append(reaction)
        
        return reactions
    

    @classmethod
    def relations(cls) -> typing.List[typing.List[str]]: 
        beautiful_soup: bs4.BeautifulSoup = cls.beautiful_soup()

        relations: typing.List = []

        for div in beautiful_soup.find_all('div', attrs={'class': 'list'}):
            for relation in div.text.split('\n'):
                if relation != '':
                    print(relation)

        return relations



Pathway.relations()


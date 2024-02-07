import bs4
import requests
import typing


class Pathway:
    def __init__(self) -> None:
        self.__html: bs4.BeautifulSoup = Pathway.__beautiful_soup()


    @staticmethod
    def __response() -> str:
        URL: str = 'https://www.kegg.jp/kegg/pathway.html'

        response: requests.Response = requests.get(URL)
        response.raise_for_status()

        return response.text
        
    
    @staticmethod
    def __beautiful_soup() -> bs4.BeautifulSoup:
        markup: str = Pathway.__response()
        features: str = 'html.parser'

        return bs4.BeautifulSoup(markup, features)
    

    def interactions(self) -> typing.List[str]:
        interactions: typing.List = []

        for h4 in self.__html.find_all('h4', attrs={'id': True}):
            interaction: str = h4.text.split('.')[0]
            interactions.append(interaction)

        return interactions
    

    def reactions(self) -> typing.List[str]:
        reactions: typing.List = []

        for b in self.__html.find_all('b')[8:]:
            reaction: str = b.text.split()[0]
            reactions.append(reaction)
        
        return reactions
    

    def relations(self) -> typing.List[typing.List[str]]: 
        relations: typing.List = []

        for div in self.__html.find_all('div', attrs={'class': 'list'}):
            relation: typing.List[str] = [relation[:5] for relation in div.text.split('\n') if relation != '']
            relations.append(relation)
            
        return relations
    
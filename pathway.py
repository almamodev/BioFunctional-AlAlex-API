import bs4
import requests
import typing

class Pathway:
    def __init__(self) -> None:
        self.__html: bs4.BeautifulSoup = Pathway.__beautiful_soup()

    @staticmethod
    def __response() -> str:
        """
        :return:
        """
        url: str = 'https://www.kegg.jp/kegg/pathway.html'

        response: requests.Response = requests.get(url)
        response.raise_for_status()

        return response.text
        
    @staticmethod
    def __beautiful_soup() -> bs4.BeautifulSoup:
        """
        :return:
        """
        markup: str = Pathway.__response()
        features: str = 'html.parser'

        return bs4.BeautifulSoup(markup, features)
    
    def __interaction(self) -> typing.List[str]:
        """
        :return:
        """
        name: str = 'h4'
        attrs: typing.Dict[str, bool] = {'id': True}

        collection: typing.List = []

        for element in self.__html.find_all(name, attrs):
            element: typing.List[str] = element.text.split(maxsplit=1)

            interaction: typing.Dict[str, str] = {
                'entry': element[0][0],
                'name': element[1]
            }
            collection.append(interaction)

        return collection

    def __reaction(self) -> typing.List[str]:
        """
        :return:
        """
        name: str = 'b'

        collection: typing.List = []

        for element in self.__html.find_all(name)[8:]:
            element: typing.List[str] = element.text.split(maxsplit=1)

            reaction: typing.Dict[str, str] = {
                'entry': element[0],
                'name': element[1]
            }
            collection.append(reaction)
        
        return collection
    
    def __relation(self) -> typing.List[typing.List[str]]: 
        """
        :return:
        """
        name: str = 'div'
        attrs: typing.Dict[str, str] = {'class': 'list'}

        collection: typing.List = []
        
        for element in self.__html.find_all(name, attrs):
            element: typing.List[str] = element.text.split('\n')

            relation: typing.List[str] = [relation[:5] for relation in element if relation != '']
            collection.append(relation)
            
        return collection

    def collection(self) -> typing.List[typing.Dict[str, str]]:
        """
        :return:
        """
        collection: typing.List = []

        for interaction in self.__interaction():
            for index, reaction in enumerate(self.__reaction()):
                if reaction['entry'].startswith(interaction['entry']):
                    for relation in self.__relation()[index]:
                        pathway: typing.Dict[str, str] = {
                            'interaction': interaction,
                            'reaction': reaction,
                            'relation': relation
                        }
                        collection.append(pathway)
        
        return collection
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
    
    def __interactions(self) -> typing.List[str]:
        """
        :return:
        """
        name: str = 'h4'
        attrs: typing.Dict[str, bool] = {'id': True}

        interactions: typing.List = []

        for element in self.__html.find_all(name, attrs):
            element: typing.List[str] = element.text.split(maxsplit=1)

            interaction: typing.Dict[str, str] = {
                'entry': element[0][0],
                'name': element[1]
            }
            interactions.append(interaction)

        return interactions

    def __reactions(self) -> typing.List[str]:
        """
        :return:
        """
        name: str = 'b'

        reactions: typing.List = []

        for element in self.__html.find_all(name)[8:]:
            element: typing.List[str] = element.text.split(maxsplit=1)

            reaction: typing.Dict[str, str] = {
                'entry': element[0],
                'name': element[1]
            }
            reactions.append(reaction)

        return reactions
    
    def __relations(self) -> typing.List[typing.List[str]]: 
        """
        :return:
        """
        name: str = 'div'
        attrs: typing.Dict[str, str] = {'class': 'list'}

        relations: typing.List = []

        for element in self.__html.find_all(name, attrs):
            element: typing.List[str] = element.text.split('\n')

            relation: typing.List[str] = [relation[:5] for relation in element if relation != '']
            relations.append(relation)

        return relations

    def collection(self) -> typing.List[typing.Dict[str, str]]:
        """
        :return:
        """
        collection: typing.List = []

        for interaction in self.__interactions():
            for index, reaction in enumerate(self.__reactions()):
                if reaction['entry'].startswith(interaction['entry']):
                    for relation in self.__relations()[index]:
                        pathway: typing.Dict[str, str] = {
                            'interaction': interaction,
                            'reaction': reaction,
                            'relation': relation
                        }
                        collection.append(pathway)
                        
        return collection
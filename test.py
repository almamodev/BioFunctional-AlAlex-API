from pathway import Pathway
import typing


def update(
    pathway: Pathway, 
    records: typing.List[typing.Dict[str, typing.Any]], 
    key: str
) -> typing.List[typing.Dict[str, typing.Any]]:
    for pathway in pathway.collection():
        for record in records:
            if record[key][2:] == pathway['relation']:
                record['interaction_entry'] = pathway['interaction']['entry']
                record['reaction_entry'] = pathway['reaction']['entry']
                record['interaction_name'] = pathway['interaction']['name']
                record['reaction_name'] = pathway['reaction']['name']
    return records


    




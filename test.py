from pathway import Pathway
import pandas
import typing

df = pandas.read_csv('dataset.csv')

def mapping(collection: Pathway.collection, df: pandas.DataFrame, column: str):
    for pathway in collection:
        for _, row in df.iterrows():
            if row[column][2:] in pathway['relation']:
                df['interaction_entry'] = pathway['interaction']['entry']
                df['interaction_name'] = pathway['interaction']['name']
                df['reaction_entry'] = pathway['reaction']['entry']
                df['reaction_name'] = pathway['reaction']['name']
    df.to_csv('dataset_filtrado.csv')

 
pathway = Pathway()
mapping(pathway.collection(), df, 'ONTOLOGY')


    




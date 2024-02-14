import typing
import csv

class Parser:
    def __init__(self, filename: str) -> None:
        """
        Initializes the Parser object with the given filename.

        :filename: The name of the file to parse.
        """
        self.__filename: str = filename

    def writer(self, rowdicts: typing.List[typing.Dict[str, typing.Any]]) -> None:
        """
        Writes the content of rowdicts to the file.

        :rowdicts: A list of dictionaries representing rows of data.
        """
        file: str = self.__filename
        mode: str = 'w'
        newline: str = ''
        with open(file, mode, newline=newline) as f:
            fieldnames: typing.List[str] = list(rowdicts[0].keys())
            writer: csv.DictWriter = csv.DictWriter(f, fieldnames)
            writer.writeheader()
            writer.writerows(rowdicts)
            
    def reader(self) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Reads the content of the file and returns it as a list of dictionaries.

        :return: A list of dictionaries containing the data from the file.
        """
        file: str = self.__filename
        mode: str = 'r'
        newline: str = ''
        with open(file, mode, newline=newline) as f:
            reader: csv.DictReader = csv.DictReader(f)
            rowdicts: typing.List[typing.Dict[str, typing.Any]] = []
            for row in reader:
                rowdicts.append(row)
        return rowdicts
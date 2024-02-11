import typing
import csv
import werkzeug.datastructures
import io

class Parse:
    def __init__(self, file: str) -> None:
        self.__file = file

    def writer(self, rowdicts: typing.List[typing.Dict[str, typing.Any]]) -> None:
        """
        :rowdicts:
        """
        fieldnames: typing.List[str] = list(rowdicts[0].keys())
        with open(self.__file, 'w', newline='') as f:
            writer: csv.DictWriter = csv.DictWriter(f, fieldnames)
            writer.writeheader()
            writer.writerows(rowdicts)
            
    def reader(self) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        :return:        
        """
        rowdicts: typing.List[typing.Dict[str, typing.Any]] = []
        with open(self.__file, 'r', newline='') as f:
            reader: csv.DictReader = csv.DictReader(f)
            for row in reader:
                rowdicts.append(row)
        return rowdicts
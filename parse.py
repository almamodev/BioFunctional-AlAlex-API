import typing
import csv
import werkzeug.datastructures

class Parse:
    def __init__(self, files: werkzeug.datastructures.FileStorage) -> None:
        self.__files = files

    def writer(self, rowdicts: typing.List[typing.Dict[str, typing.Any]]) -> None:
        """
        :rowdicts:
        """
        with open(self.__files, 'w', newline='') as f:
            fieldnames: typing.List[str] = rowdicts[0].keys()

            writer: csv.DictWriter = csv.DictWriter(f, fieldnames)

            writer.writeheader()
            writer.writerows(rowdicts)
            
    def reader(self) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        :return:        
        """
        rowdicts: typing.List = []

        with open(self.__files, 'r', newline='') as f:
            reader: csv.DictReader = csv.DictReader(f)

            for row in reader:
                rowdicts.append(row)

        return rowdicts
from ofxstatement.plugin import Plugin
from ofxstatement.parser import CsvStatementParser
from ofxstatement.statement import StatementLine


class AsnPlugin(Plugin):
    """Sample plugin (for developers only)
    """

    def get_parser(self, filename):
        f = open(
            filename, 'r', encoding=self.settings.get("charset", "UTF-8"))
        return AsnParser(f)


class AsnParser(CsvStatementParser):

    date_format = "%d-%m-%Y"
    mappings = {
        'date': 0,
        #'payee': 3,
        'memo': 17,
        'amount': 10,
        #'trntype': 14,
        'refnum': 15,
    }

    def parse(self):
        """Main entry point for parsers

        super() implementation will call to split_records and parse_record to
        process the file.
        """
        return super().parse()

    def split_records(self):
        """Return iterable object consisting of a line per transaction
        """
        return super().split_records()

    def parse_record(self, line):
        """Parse given transaction line and return StatementLine object
        """
        result = super().parse_record(line)
        if result.amount < 0:
            result.payee = line[2]
            result.trntype = 'DEBIT'
        else:
            result.payee = line[1]
            result.trntype = 'CREDIT'
        return result

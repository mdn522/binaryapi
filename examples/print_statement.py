# Print statement - https://api.deriv.com/api-explorer/#statement
import os
import time
import logging
import traceback
from rich import print
from rich.console import Console
from rich.table import Table

from binaryapi.stable_api import Binary

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

token = os.environ.get('BINARY_TOKEN', '<YOUR BINARY TOKEN GOES HERE>')
console = Console()


def message_handler(message):
    msg_type = message.get('msg_type')

    try:
        if msg_type == 'statement':
            statement = message['statement']

            table = Table(title="Statements ({})".format(statement['count']))

            table.add_column("Tx. ID", no_wrap=True)
            table.add_column("Currency", no_wrap=True)
            table.add_column("Transaction Time", no_wrap=True)
            table.add_column("Transaction", no_wrap=True)
            table.add_column("Credit/Debit", no_wrap=True)
            table.add_column("Balance", no_wrap=True)

            for tx in statement['transactions']:
                table.add_row(
                    str(tx['transaction_id']),
                    binary.api.profile.currency,
                    str(tx['transaction_time']),
                    tx['action_type'],
                    str(tx['amount']),
                    str(tx['balance_after'])
                )

            console.print(table)



    except Exception as e:
        traceback.print_exc()


if __name__ == '__main__':
    binary = Binary(token=token, message_callback=message_handler)
    print('Logged in')

    # DOC: https://api.deriv.com/api-explorer/#statement
    req_id = binary.api.statement(
        limit=10
    )

    time.sleep(5)

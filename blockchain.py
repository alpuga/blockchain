import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid

from flask import Flask


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create the genesis Block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self):
        """
        Create a new block in the Blockchain

        :param proof: <int> the proog given by the Proof of Work algo
        :param previous_hash: (optional) <str> Hash of the previous Block
        :return: <dict> New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        # Reset the current list of current_transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Blockchain

        :param sender: <str> Address of the sender
        :param recipient: <str> Address of the recipient
        :param amount: <int> amount
        :return: <int> the index of the block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1


@property
def last_block(self):
    return self.chain[-1]


@staticmethod
def hash(block):
    """
    Creates a SHA-256 hash of a Blockchain

    :param block: <dict> Block
    :return: <str>
    """

    # Make sure the dictionary is ordered, or there will be inconsistent hashes
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()


def proof_of_work(self, last_proof):
    """
    Simple Proof of Work Algorithm:
    - Find a number p' such that hash(pp') contains leading 4 zeroes,
    where p is the previous p'
    - p is the previous proof, and p' is the new proof

    :param last_proof: <int>
    :return: <int>
    """

    proof = 0
    while self.valid_proof(last_proof, proof) is False:
        proof += 1

    return proof


@staticmethod
def valid_proof(last_proof, proof):
    """
    Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?

    :param last_proof: <int> Previous proof
    :param proof: <int> Current Proof
    :return <bool> True if correct, False if not.
    """

    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"

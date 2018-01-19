# Import modules
import hashlib
import json
from time import time


##########################
# Define class
##########################
class Blockchain(object):
	"""
	"""
	def __init__(self):
		self.chain = []
		self.current_transactions = []
		
		self.new_block(proof=100, previous_hash=1)

	def new_block(self, proof, previous_hash=None):
		'''Create a new block and add it to the chain.'''
		block = {
			'index': len(self.chain) + 1,
			'timestamp': time(),
			'transactions': self.current_transactions,
			'proof': proof,
			'previous_hash': previous_hash or self.hash(self.chain[-1])
			}
		self.current_transactions = []
		self.chain.append(block)
		return block

	def new_transaction(self, sender, recipient, amount):
		'''Add a new transaction to the list of current transactions.'''	
		transaction = {
			'sender': sender,
			'recipient': recipient,
			'amount': amount
			}
		self.current_transactions.append(transaction)
		
		return self.last_block['index'] + 1

	@property
	def last_block(self):
		'''Return the last block in the chain.'''
		return self.chain[-1]

	@staticmethod
	def hash(block):
		'''Hash a block.'''
		b_string = json.dumps(block, sort_keys=True).encode()
		return hashlib.sha256(b_string).hexdigest()





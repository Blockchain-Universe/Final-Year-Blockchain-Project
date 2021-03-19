

# **TOP CLASS BLOCKCHAIN PROJECT**

**Blockchain** is a sequential chain of records called Blocks. They can contain transactions, files, information, records or any data you like, really.
But the important thing is that they’re chained together using hashes.

See my friend,
I will explain point to point this project.

If you are still not able to understand.

I will send you PPT, Project Report and Video Explanation of this Project.

Mail me at **vatshayan007@gmail.com** to get this Full Project.
"""

pip install Flask==0.12.2 requests==2.18.4

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        
    def new_block(self):
        # Creates a new Block and adds it to the chain
        pass
    
    def new_transaction(self):
        # Adds a new transaction to the list of transactions
        pass
    
    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass

block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}

class Blockchain(object):
    ...
    
    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1



"""WAIT WAIT,

Full Project Code and Report.

Please Mail me at **vatshayan007@gmail.com**
"""


'''

The task involves writing a function to display Bitcoin transaction history. The function must adhere to specific formatting requirements. Follow-up questions include implementing features to cancel and pause transactions, as well as a feature to cancel all transactions for a particular user. There will also be questions about handling streaming data.
You are given a set of transaction histories to filter by time, user, and currency. The interviewer will discuss optimization strategies and then inquire about implementing pagination for the results.

'''

'''
we have transactions and users.

each users have a set of transactions.

each transaction is associated with a user.
'''
from dataclasses import dataclass
from collections import defaultdict
from enum import Enum 
import heapq

class Currency(Enum):
    USD = "USD"
    BTC = "BTC"

class Status(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    PAUSED = "PAUSED"

class Transaction:

    def __init__(self, id: str, amount: int, timestamp: int, user: str, currency: str):
        self.id =  id
        self.amount = amount
        self.timestamp = timestamp
        self.user = user 
        self.currency = Currency(currency)
        self.status = Status.IN_PROGRESS

class User:

    def __init__(self, id: str, transactions: list):
        self.id = str
        self.transactions = transactions # list of ids
        self.idx = 0 # keep track of up to what index was last returned.

'''
1. User makes transaction. That transaction is marked as inprogress. After 2 hours (timestamp+2), we should mark that 
transaction as complete.
'''
class TransactionHistory:

    def __init__(self):
        # id -> User
        self.users = {}
        # id - > Transaction
        self.transactions = {}
        # min-heap. If current timestamp is greater than head + 2, we should pop it, then mark it as in progress. in our transaction map.
        # (timestamp, transaction_id)
        self.inProgressTransactions = [] 
        self.maxResponseCt = 50

    def processInProgressTransactions(self, timestamp_x):
        backlog = []
        while self.inProgressTransactions and self.inProgressTransactions[0][0] + 2 <= timestamp_x:
            timestamp, transaction_id = heapq.heappop(self.inProgressTransactions)
            status = self.transactions[transaction_id].status
            match status:
                case Status.PAUSED:
                    # add this back to the heap after.
                    backlog.append((timestamp, transaction_id))
                case Status.IN_PROGRESS:
                    print(f"Updating transaction {transaction_id} at timestamp {timestamp} given it is now {timestamp_x}")
                    self.transactions[transaction_id].status = Status.COMPLETED
                    # don't need to update user because user only stores transaction Ids.
                case Status.CANCELLED:
                    # do nothing, we just remove it from the queue of transactions that need to be processed.
                    pass
                case _: 
                    # we won't ever see Status.Completed on the queue.
                    pass 
        # process these later when they're in progress
        for t in backlog:
            heapq.heappush(self.inProgressTransactions, t)
    
    def addTransactionToUser(self, id, amount, timestamp, user, currency):
        # assuming all transaction ids we see are unique. if not then we need to make self.transactions[user] a map.
        self.processInProgressTransactions(timestamp)

        if user not in self.users:
            self.users[user] = User(user, [])

        self.users[user].transactions.append(id)
        
        t = Transaction(id, amount, timestamp, user, currency)

        self.transactions[id] = t

        heapq.heappush(self.inProgressTransactions, (timestamp, id))

    '''
    If a transaction is in progress, pause it and don't process it. 
    '''
    def pauseTransaction(self, timestamp, id):
        self.transactions[id].status = Status.PAUSED

        self.processInProgressTransactions(timestamp)

    '''
    Cancel it, meaning don't process it when it's timestamp is appropriate.
    '''
    def cancelTransaction(self, timestamp, id):
        self.transactions[id].status = Status.CANCELLED

        self.processInProgressTransactions(timestamp)

    def cancelAllTransactionsForAUser(self, timestamp, user):
        for t in self.users[user].transactions:
            t.status = Status.CANCELLED

        self.processInProgressTransactions(timestamp)

    def getAllTransactionsForAUser(self, user):
        currIdx = user.idx
        transactions = self.users[user].transactions[i]

        res = []
        for i in range(user.idx, min(currIdx+self.maxResponseCt, len(transactions))):
            res.append(transactions[i])

    '''
    Get all transactions for all users before a certain timestamp.
    Return the transaction as:
    (timestamp, user, id)
    where transactions are sorted by descending timestamp. for the same timestamp, return by increasing user_id.
    '''
    def getAllTransactionsBeforeTime(self, timestamp):
        self.processInProgressTransactions(timestamp)

        # [ (timestamp, user, transaction_id, status)]
        res = []
        for t in self.transactions.values(): # transaction_id -> Timestamp
            if t.timestamp < timestamp:
                res.append((t.timestamp, t.user, t.id, t.status))
        return sorted(res, key=lambda x:(-x[0], x[1], x[2], x[3]))

import unittest 

class TransactionHistoryTest(unittest.TestCase):

    def testProcessTransactions(self):
        history = TransactionHistory()
        history.addTransactionToUser("Transaction1", 5.0, 1, "User1", "USD")
        history.addTransactionToUser("Transaction2", 10.0, 2, "User1", "BTC")
        history.pauseTransaction(3, "Transaction2")

        print(history.getAllTransactionsBeforeTime(10)) # transaction1 should be complete and transaction 2 should be paused.
        
if __name__ == '__main__':
    unittest.main()




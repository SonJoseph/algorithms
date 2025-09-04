You are given a snapshot of an order book with bids and asks for a currency pair (e.g., USD/ETH), and you need to simulate an exchange.

bids = [(101, 5), (100, 10)]
asks = [(99, 4), (100, 3), (102, 7)]

'''
buy of 5 orders at price 101.
matched with lowest sell of 99 for 4 orders.

for buy_amt, buy_price  in bids:
    while sell_q and buy_amt > 0:
        if sell_q[0][0] < buy_price:
            sell_price, sell_amt = heapq.heappop(sell_q)
            trade_amt = min(buy_amt, sell_amt) 
            buy_amt -= trade_amt
            sell_amt -= trade_amt

            if sell_amt > 0:
                heapq.heappush(sell, (sell_price, sell_amt))


in a streaming context,
we'd need to add the bids and asks to individual queues. once they're added to the queue. process the requests.

'''
def match_orders(bids, asks)
    # returns (total_volume_in_usd, total_asset_amount_traded)

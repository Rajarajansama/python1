class bank:
	def __init__(self,withdraw):
		self.withdraw=withdraw
	def __sub__(self,amount):
		return self.withdraw-amount.withdraw
w=bank(1000)
w1=bank(500)
print('withdraw amount is',w-w1)

 output: withdraw amount is 500
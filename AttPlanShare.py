import math

############### Account Info Summary #####################
Account_List = ['0915' , '0896' , '7001' , '5076']	# Account members' numbers
BasicData = 10
BasicDataFee = 105
ExtraDataFee = input("What's the extra data usage fee(unit: $)?")
DataShare = range(len(Account_List))
BasicFee = range(len(Account_List))
for i in range(len(Account_List)):	# Enter the share info for each number
	print("--------------------------------")
	print("Current Account: ")
	print(Account_List[i])
	DataShare[i] = input("Data Share Percentage(unit: %)?")
	DataShare[i] = float(DataShare[i])
	BasicFee[i] = input("Basic payment(unit: $)?")
	BasicFee[i] = float(BasicFee[i])

############### Payment Calculation #####################
PaymentList = range(len(Account_List))
ExtraDataShare = range(len(Account_List))
for j in range(len(Account_List)):
	if DataShare[j] > (1/len(Account_List)):
		ExtraDataShare[j] = DataShare[j]
	else:
		ExtraDataShare[j] = 0
ExtraDataShareSum = 0
for j in range(len(Account_List)):
	ExtraDataShareSum = ExtraDataShareSum + ExtraDataShare[j]
for j in range(len(Account_List)):
	PaymentList[j] = BasicFee[j] + (BasicDataFee / len(Account_List)) + (int(ExtraDataFee) * (ExtraDataShare[j] / ExtraDataShareSum))

############### Print Payment #####################
print("---------------------------------------------")
print("Print Payment")
for k in range(len(Account_List)):
	print("***")
	print('Payment ($) for', Account_List[k])
	print(PaymentList[k])

class Budget:
    def __init__(self,category):
        self.category = category
        self.balance = 0


    def options(self):
        print ('''''
        1. Deposit
        2. Withdrawal
        3. Current Balance
        4. Transfer
        5. Cancel
        ''''')

        selectedoption = input(int('Please Enter Your Prefered Option \n'))

        while True:
            if selectedoption == 1:
                self.deposit()
                break

            elif selectedoption == 2:
                self.withdrawal()
                break

            elif selectedoption == 3:
                self.currentbalance()
                break

            elif selectedoption == 4:
                self.transfer()
                break
            
            elif selectedoption == 5:
                print('Thank you for visiting Zuri! Goodbye!')
                break

            else:
                print('Invalid Option! Pls Try again')
                selectedoption = input(int('Please Enter Your Prefered Option \n'))
                



    
    def deposit(self):
        print(f'Hello! make a deposit into {self.category} in Naira \n')
        amount = int(input('Kindly enter amount to deposit \n'))
        self.balance += amount
        print(f' Deposit of {amount} into {self.category} was successful')



    def withdrawal(self):
        print(f'Hello! make a deposit into {self.category} in Naira \n')
        amount = int(input('Kindly enter amount to withdraw \n'))
        if self.balance >= amount:

            if amount >= 500:
                self.balance -= amount
                print(f' Withdrawal of {amount} from {self.category} was successful')
            else:
                print('Withdrawal amount can not be less than 500 NGN. Please Try Again')
                self.withdrawal()

        else:
            print(f'Insufficient Funds! Pls fund this {self.category} and try again')
            self.options()
        
    def currentbalance(self):
        return (f'Your current balance is {self.balance}')
    
    def transfer(self):
        print('Please enter amount you want to transfer \n')
        transfer_amount = int(input('Amount in Naira \n'))
        if self.balance >= transfer_amount:
            print('Please select a category to transfer to \n')
            print(f'''
			1. {food.category}
			2. {clothing.category}
			3. {entertainment.category}
			''')
            preferred_option = int(input('Enter your Preferred Option \n'))
            while True:
                if preferred_option == 1:
                    print(f'NGN {transfer_amount} has been transferred into {food.category}. Thank you! \n')
                    self.balance -= transfer_amount
                    break
                
                elif preferred_option == 2:
                    print(f'NGN {transfer_amount} has been transferred into {clothing.category}. Thank you! \n')
                    self.balance -= transfer_amount
                    break

                elif preferred_option == 3:
                    print(f'NGN {transfer_amount} has been transferred into {clothing.category}. Thank you! \n')
                    self.balance -= transfer_amount
                    break
                else:
                    print('Invalid Selection, Please Try Again')
                    preferred_option = int(input('Enter your Preferred Option \n'))
                    break

            else:
                print(' No transfer was made. Insufficient Funds')
                self.options()

        
food = Budget('Food')
clothing = Budget('Clothing')
entertainment = Budget('Entertainment')


print(' Welcome! Time to have fun budgetting!')
print(f""" 1. {food.category} 
2. {clothing.category}   
3. {entertainment.category}
4. Cancel
""")

category = int(input('Please, Select a Category :\n'))

while True:
		if category == 1:
			print(f'{food.category}\n')
			food.options()
			continue

		elif category == 2:
			print(f'{clothing.category}\n')
			clothing.options()
			continue

		elif category == 3:
			print(f'{entertainment.category}\n')
			entertainment.options()
			continue

		elif category == 4:
			print('Thanks for choosing us! Goodbye')
			break
		else:
			print('Invalid Selection, Please Try Again')
			category = int(input('Please, Select a Category: \n'))
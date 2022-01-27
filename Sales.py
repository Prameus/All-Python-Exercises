from dataclasses import dataclass
from json import loads, dumps
import datetime
import random
import asyncio

@dataclass
class Personels:
    name: str
    surname: str
    commition: float = 10


@dataclass
class Sales:
    personel: str
    company: str
    sale_date: str


class Management:
    time = datetime.datetime.now()
    personel_list = ['hari seldon', 'dors venabili',
                     'anakin skywalker', 'freddy kruger']
    company_list = ['siemens', 'TDK', 'apple', 'chineese communist party']
    first_dict = {'hari seldon': None, 'dors venabili': None,
                  'anakin skywalker': None, 'freddy kruger': None}
    last_dict = []
    skyrim_guard_quotes = [
        "I used to be an adventurer like you. Then I took an arrow in the knee...",
        "Let me guess... someone stole your sweetroll.",
        "My cousin's out fighting dragons, and what do I get? Guard duty.",
        "Stay out of trouble, Elf.",
        "hey you're finally awake",
        "Stop right there, criminal scum! Nobody breaks the law on my watch!"]
    commution = 10
    price = 1000

    def sales_screen(self):
        while True:
            choice = str(input(
                'if you want enter to;\n personel`s panel write "personel",\n Purcase panel write "purcase",\n To see all buying of company write "company"\nFor quit write "quit"\n Your action?: '))
            if choice == 'personel':
                self.personels_screen()
            elif choice == 'purcase':
                self.purcase_screen()
            elif choice == 'company':
                self.company_screen()
            elif choice == 'quit':
                break
            else:
                print(random.choice(self.skyrim_guard_quotes))

    def personels_screen(self):
        choosen_personel = str(
            input('First, choose which personel you want to work with: '))
        personel = self.first_dict[choosen_personel]
        print(personel)
        choice = (input(
            'Please provide your action as;\n To see choosen personels commution write "commution"\n To see choosen personels ALL commution write "all commution": '))
        if choice == 'all commution':
            total_commution = 0
            for i in personel:
                commution_of_personel = i[1]
                total_commution = total_commution + commution_of_personel
                print(
                    f"{total_commution}, Here is {choosen_personel}`s summation of his/her all commution")
        else:
            print(random.choice(self.skyrim_guard_quotes))

    def check_company(self, company):
        bill = []
        field = self.first_dict.values()
        for i in field:
            if i[0] == company:
                bill.append(i[0])
        return bill

    def company_screen(self):
        choice = str(
            input('Please write the company you want to see all payments'))
        bill = self.check_company(choice)
        print(f'here is all information of {bill} named company`s payment')

    def purcase_screen(self):
        while True:
            confirmed_personel = self.confirm_personel()
            confirmed_company = self.confirm_company()
            changed_commution = self.commution_changer(confirmed_personel)
            sold_price = self.sale_calculater()
            print(
                f'Thanks for working with us! This service cost you {sold_price}! ')
            time_now = str(self.time.strftime("%b %d, %Y"))
            print(time_now)
            self.last_dict.append((confirmed_company, sold_price, time_now))
            self.check_personel(confirmed_personel, self.last_dict)
            print(f"Here is your bill!\n{self.first_dict}")
            break

    def check_personel(self, personel, last_dict):
        for i in self.first_dict.keys():
            if i == personel:
                self.first_dict.update({i: last_dict})

    def confirm_personel(self):
        while True:
            personel = str(input(
                f'{self.personel_list}\n Hello There! Which personel would you like to work? : '))
            for workers in self.personel_list:
                if workers == personel:
                    print(f'We are sending {personel}!')
                    return personel
            print(
                f'There isnt any personel named: {personel}! Please try again')

    def confirm_company(self):
        while True:
            company = str(
                input(f'General Kenobi! I mean hello there, Which company you working for? There is a list if you can`t remember. \n{self.company_list}\n do you regain knowledge about your master?: '))
            for companys in self.company_list:
                if companys == company:
                    return company
            print(
                f'There is not such as company named {company}?? Are you a spy?')

    def commution_changer(self, personel):
        while True:
            choice = str(input(
                f'Do you want to change commution of {personel}? Write "yes" or "no" '))
            if choice == 'yes':
                self.commution = float(input(
                    f'Please enter the new commution of {personel}'))
                break
            else:
                break

    def sale_calculater(self):
        operation = (self.price+(self.price/self.commution))
        return operation

    def write_to_dictionary(self, personel):
        second_dict = {}
        for k, v in self.data_dict.items():
            self.data_dict

    def write_to_json(self):
        with open('bill.json', 'w') as f:
            f.write(dumps())


management = Management()
management.sales_screen()

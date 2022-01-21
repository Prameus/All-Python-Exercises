from dataclasses import dataclass
from json import loads, dumps
import datetime
from operator import indexOf
import random


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
    first_dict = {}
    last_dict = []
    skyrim_guard_quotes = [
        "I used to be an adventurer like you. Then I took an arrow in the knee...", "Let me guess... someone stole your sweetroll.", "My cousin's out fighting dragons, and what do I get? Guard duty.", "Stay out of trouble, Elf."]
    commution = 10
    price = 1000

    def sales_screen(self):
        while True:
            choice = str(input(
                'if you want enter to;\n personel`s panel write "personel",\n Purcase panel write "purcase",\nFor quit write "quit"\n Your action?: '))
            if choice == 'personel':
                self.personels_screen()
            elif choice == 'purcase':
                self.manage()
            elif choice == 'quit':
                break
            else:
                print(random.choice(self.skyrim_guard_quotes))

    def personels_screen(self):
        commution = []
        choosen_personel = str(
            input('First, choose which personel you want to work with: '))
        personel = self.first_dict[choosen_personel]
        choice = str(input(
            'Please provide your action as;\n To see choosen personels commution write "commution"\n To see choosen personels ALL commution write "all commution"'))
        if choice == 'commution':
            pass

        elif choice == 'all commution':
            pass
        for i in self.first_dict.values():
            commution.append(i[1])
            print(commution)

    def manage(self):
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

            self.first_dict.update({confirmed_personel: self.last_dict})
            print(f"Here is your bill!\n{self.first_dict}")
            break

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
        operation = str(self.price+(self.price/self.commution))
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

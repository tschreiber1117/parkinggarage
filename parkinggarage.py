class parking_garage:


    def __init__(self, tickets = ['ticket','ticket','ticket'], parking_spaces = ['spaces','spaces','spaces'], current_ticket = {'paid':False}):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = current_ticket

    def take_ticket(self):
        self.tickets.remove('ticket')
        self.parking_spaces.remove('spaces')

    def payForParking(self):
        payment = input('Pay for your ticket, please: ')
        if payment != '':
            print('Thank you for parking, you have 15 minutes of parking time.')
            current_ticket['paid'] = True

    def leaveGarage(self):
        if self.payment != '':
            print('Thank you, have a nice day')
        else:
            self.payForParking()
        self.tickets.append('ticket')
        self.parking_spaces('spaces')
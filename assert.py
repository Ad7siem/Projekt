import datetime

netto = 100
brutto = 120
# netto must be less or equal to brutto
assert netto <= brutto, 'Netto cannot be greater then brutto'

orderData = datetime.date(2022,10,13)
deliveryDate = datetime.date(2022,10,18)
# order date should be earlier then the delivery date
assert orderData <= deliveryDate, 'Order date cannot be later than delivery date'

print('-'*30,'\n')

# ćwiczenia

import datetime as dt


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        assert len(self.title) > 0, 'Title is empty!'
        assert self.start <= self.end, 'Start date is later than end date!'

    @classmethod
    def publish_offer(cls, trips):
        list_of_errors = []
        for trip in trips:
            try:
                trip.check_data()
            except ValueError as e:
                list_of_errors.append('{} {}'.format(trip.symbol, str(e)))
            except Exception as e:
                list_of_errors.append('{} {}'.format(trip.symbol, str(e)))

        assert len(list_of_errors) < 0, 'The list of trips has errors: {}'.format(list_of_errors)
        print('The offer will be published...')


trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
]

try:
    print('Publishing trips...')
    Trip.publish_offer(trips)
    print('...done')
except Exception as e:
    print('Ohh noo!!! Error Trips.\n{}'.format(e))
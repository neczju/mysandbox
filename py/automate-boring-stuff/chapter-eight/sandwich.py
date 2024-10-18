import pyinputplus as pyip

def sandwich_calculation(sandwich, extra, amount):
    sandwich_prices = {'bread_type': {'wheat': 4.98, 'white': 3.99, 'sourdough': 5.18},
                      'protein_type': {'chiken': 1.28, 'turkey': 1.40, 'ham': 1.50, 'tofu': 2.04},
                      'cheese_type': {'cheddar': 2.50, 'swiss': 3.00, 'mozzarella': 2.44}}
    sandwich_extra_prices = {'mayonnaise': 0.58,
                             'mustard': 0.77,
                             'lettuce': 0.99,
                             'tomato': 0.98}


    sandwich_price = 0
    for key, value in sandwich.items():
        print(value + str(sandwich_prices[key][value]).rjust(15, '.'))
        sandwich_price += sandwich_prices[key][value]

    for key, value in extra.items():
        if value == 'yes':
            print(key + str(sandwich_extra_prices[key]).rjust(15, '.'))
            sandwich_price += sandwich_extra_prices[key]

    print('Price: %.2f PLN' % (sandwich_price * amount))


sandwich_types = {}
sandwich_types['bread_type'] = pyip.inputMenu(['wheat', 'white', 'sourdough'], 'Choose the type of bread\n')
sandwich_types['protein_type'] = pyip.inputMenu(['chiken', 'turkey', 'ham', 'tofu'], 'Choose protein type\n')

cheese = pyip.inputYesNo('Should I add cheese? ')
if cheese == 'yes':
    sandwich_types['cheese_type'] = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], 'Select cheese type\n')

sandwich_extra = {}
sandwich_extra['mayonnaise'] = pyip.inputYesNo('Should I add mayonnaise? ')
sandwich_extra['mustard'] = pyip.inputYesNo('Should I add mustard? ')
sandwich_extra['lettuce'] = pyip.inputYesNo('Should I add lettuce? ')
sandwich_extra['tomato'] = pyip.inputYesNo('Should I add tomato? ')
sandwich_amount = pyip.inputInt('How many sandwiches to make? ', min=1)

sandwich_calculation(sandwich_types, sandwich_extra, sandwich_amount)

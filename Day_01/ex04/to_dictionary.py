def data():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    return dict(list_of_tuples)

def list_in_set(data_list):
    set_of_data = set(data_list)
    for key, value in set_of_data.items():
        print("\'%s\' : \'%s\'" % (value, key))

def inv_dict():
    new_dict = data()
    for key, value in new_dict.items():
        print("\'%s\' : \'%s\'" % (value, key))

if __name__ == '__main__':
    #inv_dict()
    list_in_set()
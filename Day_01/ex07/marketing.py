import sys

# Функция, которая создает список элементов первого списка, не входящих во второй
def list1_minus_list2(list1, list2):
    new_list = [x for x in list1 if x not in list2]
    return new_list

def marketing():

    # Исходные списки
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    # Соберем контакты клиентов и участников в один список для того, чтобы найти всех, кто не видел письмо
    contact_list = clients + participants
    # Уберем из этого списка повторы путем конвертации в набор(set) (набор не содержит повторяющихся элементов)
    contact_list = list(set(contact_list))

    # Выполним запрошенную задачу
    if sys.argv[1] == 'call_center':
        print(list1_minus_list2(contact_list, recipients))
    if sys.argv[1] == 'potential_clients':
        print(list1_minus_list2(participants, clients))
    if sys.argv[1] == 'loyalty_program':
        print(list1_minus_list2(clients, participants))

if __name__ == '__main__':
    # Проверим правильность аргументов
    if len (sys.argv) != 2 or (sys.argv[1] != 'calpotential_clientsl_center' and sys.argv[1] != 'potential_clients' and sys.argv[1] != 'loyalty_program'):
        raise Exception("Error argument")
    marketing()

# Вызывать с одним из аргументов potential_clients, potential_clients или loyalty_program
# https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
# https://pythonru.com/osnovy/obrabotka-iskljuchenij-python-blok-try-except-blok-finally
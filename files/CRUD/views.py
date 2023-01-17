import json
FILE_PATH = '/home/saikal/Desktop/Ev.25/files/CRUD/data.json'
ID_FILE_PATH = '/home/saikal/Desktop/Ev.25/files/CRUD/id.txt'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)

# CRUD - Reviever(read)
def list_of_products():
    data = get_data()
    return f'Список всех товаров: {data}'

def detail_product():
    data = get_data()
    try:
        id = int(input('Введите ID продукта: '))
        product = list(filter(lambda x: id == x ['id'], data))
        return product[0]
    except:
        return 'Неверный ID!'


def get_id():
    with open(ID_FILE_PATH, 'r') as file:
        id = int(file.read())
        id += 1
    with open(ID_FILE_PATH, 'w') as file:
        file.write(str(id))
    return id


def create_product():
    data = get_data()
    try:
        product = {
        'id':get_id(),
        'title': input('Введите название продукта: '),
        'price': float(input('Введите цену продукта: ')),
        'description': input('Введите описание: ')
    }
    except Exception as e:
        print(e)
        return 'Неверные данные!'
    data.append(product)
    save_data(data)
    return 'Создан новый товар!'
# print(create_product())


def update_product():
    data = get_data()
    try:
        id = int(input('Введите id продукта: '))
        product = list(filter(lambda x: x['id'] == id, data)) [0]
    except:
        return 'Неверный id!'

    index = data.index(product)
    choice = input('Что вы хотите изменить?(1-title, 2-choice, 3-description): ' )

    if choice.strip() == '1':
        data[index]['title'] = float(input('Введите новое значение для товара: '))

    elif choice.strip() == '2':
        try:
            data[index]['price'] = float(input('Введите новую цену для товара: '))
        except:
            return 'Неверное значение для цены!'

    elif choice.strip() == '3':
        data[index]['description'] = float(input('Введите новое описание для товара: '))
    else:
        return 'Неверное значение для обновления!'
        
    save_data(data)
    return 'Товар обновлен!'

# print(update_product())

def delete_product():
    data = get_data()
    try:
        id = int(input('Введите id продукта: '))
        product = list(filter(lambda x: x['id'] == id, data)) [0]
        print(f'Товар для удаления {product ["title"]}')
    except:
        return 'Неверный id!'

    choice = input('Удалить этот товар(yes/no)?')
    if choice.lowe().strip() != 'yes':
        return 'Товар не удален!'
    data.remove(product)
    save_data(data)
    return 'Товар удалён!'

1


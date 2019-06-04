class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Tv(Product):
    def __init__(self, name, price, diagonal, resolution):
        super().__init__(name, price)
        self.diagonal = diagonal
        self.resolution = resolution


class Books(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author


class Notebook(Tv):
    def __init__(self, name, price, diagonal, resolution, ram, cpu, gpu):
        super().__init__(name, price, diagonal, resolution)
        self.ram = ram
        self.cpu = cpu
        self.gpu = gpu


class Tshirt(Product):
    def __init__(self, name, price, size, colour):
        super().__init__(name, price)
        self.size = size
        self.colour = colour


def add_products(container, product):
    container.append(product)


def search_products(container, search):
    search_lowercased = search.strip().lower()
    result = []
    for product in container:
        if search_lowercased in product.name.lower():
            result.append(product)
    return result


if __name__ == '__main__':
    all_products = []
    tv = Tv('LG', 25_000, '30"', 'Full HD')
    tv2 = Tv('Samsung', 60_000, '55"', '4K')
    book = Books('War and Peace', 500, 'Tolstoy')
    book2 = Books('Evgenyi Onegin', 600, 'Pushkin')
    notebook = Notebook('ASUS', 45_000, '15"', 'Full HD', '8gb', 'i5 7th Gen', 'gtx 1050')
    notebook2 = Notebook('ASUS', 55_000, '17"', 'Full HD', '16gb', 'i7 7th Gen', 'gtx 1070')
    tshirt = Tshirt('Zara', 1000, 'XL', 'Black')
    tshirt2 = Tshirt('Lacoste', 2500, 'L', 'Green')
    print(add_products(all_products, tv))
    print(add_products(all_products, tv2))
    print(add_products(all_products, book))
    print(add_products(all_products, book2))
    print(add_products(all_products, notebook))
    print(add_products(all_products, notebook2))
    print(add_products(all_products, tshirt))
    print(add_products(all_products, tshirt2))
    # print(len(all_products))

    print(search_products(all_products, 'Samsung'))
    print(search_products(all_products, 'ASUS'))
    print(search_products(all_products, 'lacos'))

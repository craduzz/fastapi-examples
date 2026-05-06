def get_total(costs:dict, items:list[str], tax:float) -> float:
    bill = [costs.get(item, 0) for item in items]
    total = sum(bill) * (1+tax)
    return round(total, 2)

def main():
    costs = {
        'socks': 5,
        'shoes': 60,
        'sweater': 30
    }
    items = ['socks', 'shoes']

    print(get_total(costs, items, 0.09))

if __name__ == '__main__':
    main()
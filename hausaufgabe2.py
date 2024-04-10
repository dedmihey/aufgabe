price_ = 50
weight_ = int(input('Вес посылки в кг: '))
if weight_ <= 2:
    print('Стоимость доставки ', price_, 'рублей')
if weight_ > 2 and weight_ <= 10:
    for i in range(weight_ - 2):
        price_ += 20
    print('Стоимость доставки', price_)
if weight_ > 10:
    print('Стоимость доставки', 200)





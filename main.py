
def merge_list_to_dict(list1, list2):
    list1_copy = list1.copy()
    list2_copy = list2.copy()
    dict_from_lists = dict(zip(list1_copy, list2_copy))
    return dict_from_lists


list_first = ['one', 'two', 'three', 'four', 'five']
list_second = [1, 2, 3, 4, 5]

print(merge_list_to_dict(list2=list_second, list1=list_first))
print(merge_list_to_dict(list_first, list2=list_second))


def update_car_info(**car):
    car_copy = car.copy()
    print(car_copy, type(car_copy))
    car_copy['is_aveliable'] = True
    return (car_copy)


print(update_car_info(brand='bmw', version='M5', price=499))

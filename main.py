def route_info(one_dict):
    if one_dict.get('distance') and isinstance(one_dict['distance'], int):
        # if type(one_dict['distance']) == int:
        return f"Distance to your destination is {one_dict['distance']}"
    elif one_dict.get('speed') and one_dict.get('time'):
        return f"Distance to your destination is {one_dict['speed']*one_dict['time']}"
    else:
        return f"No distance info is available"


'''Если в словаре нет ключа 'distance', 
то one_dict['distance'] вызовет KeyError, 
и функция упадёт, не дойдя до elif и else.'''

print(route_info({'distance': 200, 'speed': 30, 'time': 2}))
print(route_info({'route': 'dangerous'}))
print(route_info({'speed': 80, 'time': 2}))

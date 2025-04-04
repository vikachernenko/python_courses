my_dict = {
    'image_id': 5136,
    'image_title': 'my cat'
}


def image_info(image):
    if 'image_id' not in image:
        raise NameError('the dict is not have image\'s id')
    if 'image_title' not in image:
        raise KeyError('the dict is not have image\'s title')
    else:
        return print(f"Image '{image['image_title']}' has id {image['image_id']}")


try:
    image_info(my_dict)
except NameError as e:
    print(e)
except KeyError as e:
    print(e)


from class_cat import Cat
cats = [
    {
    "name": "Барон",
    "gender": "мальчик",
    "age": 2,
    },
    {
    "name": "Сэм",
    "gender": "мальчик",
    "age": 2,
    }
]

for cat in cats:
    cat_obj = Cat()
    cat_obj.init_from_dict(cat)
    print(f'\nИмя:{cat_obj.name}', f'\nПол:{cat_obj.gender}', f'\nВозраст:{cat_obj.age}')
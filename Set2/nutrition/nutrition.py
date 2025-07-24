fruits_nutrition = {
    'apple':130,
    'avocado':50,
    'banana':110,
    'grapes':90,
    'grapefruit':60,
    'sweet cherries':100,
    'nectarine':60,
    'pear':100,
    'lemon':15,
    'honeydew melon':50,
    'lime':20,
    'peach':60,
    'orange':80,
    'kiwifruit':90,
    'cantaloupe':50,
    'tangerine':50,
    'watermelon':80,
    'sweet cherries':100,
    'strawberries':50,
    'plums':70,
    'pineapple':50
}

item = input('Item: ').lower()
calories = fruits_nutrition.get(item,'')
output = f'Calories: {calories}' if calories != "" else calories
print(output,end='')
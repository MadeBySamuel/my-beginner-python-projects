

import random

bakery = [{"name":"Bread","quantity": 0, "capacity": 50, "price": round(random.uniform(1.20,2.45),2)},
          {"name": "Bagels", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
          {"name": "Croissants", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
          {"name": "Tortillas", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
          {"name": "White rice", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
          {"name": "Brown rice", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
          {"name": "Pasta", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
          {"name": "Careal", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
]

List = [{"name": "Truck capacity", "capacity": 50, "level": 0}]


Fruit = [
    {"name":"Apple","quantity": 0, "capacity": 50, "price": round(random.uniform(1.20,2.45),2)},
    {"name":"Banana","quantity": 0,  "capacity": 50, "price": round(random.uniform(2.20,3.70),2)},
    {"name":"Orange","quantity": 0,  "capacity": 50, "price": round(random.uniform(0.20,0.60),2)},
    {"name":"Lemon","quantity": 0,  "capacity": 50, "price": round(random.uniform(4.20,8.70),2)},
    {"name":"Strawberry", "quantity": 0,  "capacity": 50, "price": round(random.uniform(3.20,10),2)},
    {"name":"Mango", "quantity": 0,  "capacity": 50, "price": round(random.uniform(4.20,10),2)},
    {"name":"Pineapple", "quantity": 0,  "capacity": 50, "price": round(random.uniform(4.20,10),2)},
    {"name":"Avocado", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
    {"name": "Coconut", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
    {"name": "Papaya", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
    {"name": "Kiwi", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
    {"name": "Pear", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},

]

Vegetable = [{"name":"Carrot","quantity": 0, "capacity": 50, "price": round(random.uniform(1.20,2.45),2)},
             {"name": "Tomato", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
             {"name": "Cucumber", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
             {"name": "Lettuce", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
             {"name": "Broccoli", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
             {"name": "Garlic", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
             {"name": "Spinach", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
             {"name": "Apple", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},

             ]

Dairy = [{"name":"Milk","quantity": 0, "capacity": 50, "price": round(random.uniform(1.20,2.45),2)},
         {"name": "Almond Milk", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
         {"name": "Butter", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
         {"name": "Cheese", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
         {"name": "Yogurt", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
         {"name": "Cottage cheese", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
         {"name": "Sour cream", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
         {"name": "Cream cheese", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
         {"name": "Whipping cream", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
         ]

Meat = [{"name":"Chicken breast","quantity": 0, "capacity": 50, "price": round(random.uniform(1.20,2.45),2)},
            {"name": "Ground beef", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
            {"name": "Pork chops", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
            {"name": "Bacon", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
            {"name": "Sausages", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
            {"name": "Ham", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
            {"name": "Turkey", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
            {"name": "Salmon", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
            {"name": "Tuna", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
            ]

Pentry = [    {"name":"Olive oil","quantity": 0, "capacity": 50, "price": round(random.uniform(1.20,2.45),2)},
              {"name": "Salt", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
              {"name": "Pepper", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
              {"name": "Sugar", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
              {"name": "Flour", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
              {"name": "Bakin powder", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
              {"name": "Vinegar", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
              {"name": "Ketchup", "quantity": 0,  "capacity": 50, "price": round(random.uniform(1.20, 2.45), 2)},
              {"name": "Mayonnaise", "quantity": 0,  "capacity": 50,"price": round(random.uniform(1.20, 2.45), 2)},
              {"name": "Mustard", "quantity": 0,  "capacity": 50,"price": round(random.uniform(1.20, 2.45), 2)},
]

Listof = {"Bakery", "Fruit", "Vegetable", "Dairy", "Meat", "Pentry"}




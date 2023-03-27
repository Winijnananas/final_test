from calculate_palm import validate_weight
from calculate_palm import calculate_price
from calculate_palm import display_price


weight_with_palm_oil = float(input("ใส่น้ำหนักของน้ำมันปาล์มกับยานพาหนะเป็นกิโลกรัม: "))
weight_empty = float(input("ใส่น้ำหนักของรถเปล่าเป็นกิโลกรัม: "))
price_per_kg = float(input("ป้อนราคาน้ำมันปาล์มต่อกิโลกรัม: "))

result = display_price(weight_with_palm_oil, weight_empty, price_per_kg)
if validate_weight(weight_with_palm_oil, weight_empty):
    price = calculate_price(weight_with_palm_oil, weight_empty, price_per_kg)
    print(f"The total weight of the palm oil is {weight_with_palm_oil - weight_empty} kg and the price is {price} baht.")
else:
    print("Weight limit exceeded. Maximum weight allowed is 3000 kg.")
    print(result)

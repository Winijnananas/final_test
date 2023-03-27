def calculate_price(weight_with_palm_oil, weight_empty, price_per_kg):
    # คำนวณราคาน้ำมันปาล์มตามน้ำหนัก น้ำหนักรถ และราคาต่อกก.
    total_weight = weight_with_palm_oil - weight_empty
    if not validate_weight(weight_with_palm_oil, weight_empty):
        return "Weight limit exceeded. Maximum weight allowed is 3000 kg."
    else:
        total_price = total_weight * price_per_kg
        return int(total_price)
def validate_weight(weight_with_palm_oil, weight_empty):
    # ตรวจสอบน้ำหนักของน้ำมันปาล์มกับรถเพื่อให้แน่ใจว่าไม่เกินน้ำหนักที่กำหนด
    total_weight = weight_with_palm_oil - weight_empty
    if total_weight > 3000:
        return False
    else:
        return True
def display_price(weight_with_palm_oil, weight_empty, price_per_kg):
    # คำนวณราคาน้ำมันปาล์มตามน้ำหนัก น้ำหนักรถ และราคาต่อกก.
    total_weight = weight_with_palm_oil - weight_empty
    if not validate_weight(weight_with_palm_oil, weight_empty):
        return "Weight limit exceeded. Maximum weight allowed is 3000 kg."
    else:
        total_price = calculate_price(weight_with_palm_oil, weight_empty, price_per_kg)
        return f"The total weight of the palm oil is {total_weight} kg and the price is {total_price} baht."

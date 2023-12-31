
gst_rates = {
        "Electronics": 0.18,
        "Clothing": 0.12,
        "Books": 0.05,
        "Furniture": 0.18,
        "Groceries": 0.0,
        "Toys": 0.12,
    }

def calculate_gst(mrp, product_type):
    
    if product_type in gst_rates:
        gst_rate = gst_rates[product_type]
        gst_amount = mrp * gst_rate
        return gst_amount
    else:
        return "Invalid product type"

def display_product_types():
    print("Available Product Types:")
    for product_type in gst_rates.keys():
        print(product_type)

mrp = float(input("Enter MRP: "))
display_product_types()
product_type = input("Enter product type: ")

gst_amount = calculate_gst(mrp, product_type)

if type(gst_amount) == float:
    print(f"GST Amount for {product_type} with MRP {mrp} is: Rs.{gst_amount:.2f}")
else:
    print(gst_amount)

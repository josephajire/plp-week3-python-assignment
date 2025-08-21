# My answer to question 1.

def calculate_discount(price, discount_percent): 
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# My answer to question 2.
try:
    # The two lines that follow prompt user for input
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # The conditional statements help to ensure that valid price and percentage are entered
    if original_price < 0:
        print("Error: Price cannot be negative.")
    elif discount < 0:
        print("Error: Discount percentage cannot be negative.")
    elif discount > 100:
        print("Error: Discount percentage cannot exceed 100%.")
    else:
        # Use the function after ensuring validation
        final_price = calculate_discount(original_price, discount)

        # Print result
        if discount >= 20:
            print(f"The final price after {discount}% discount is ${final_price:.2f}")
        else:
            print(f"Discount is not applicable. The original price is ${original_price:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values.")
def calculate_discount(price, discount_percent):
   
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get input from user
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate and display the final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Output results
    if final_price < original_price:
        print(f"A discount of {discount_percentage}% was applied.")
        print(f"Final price after discount: ${final_price:.2f}")
    else:
        print(f"No discount applied. Discount must be 20% or higher.")
        print(f"Original price: ${original_price:.2f}")
        
except ValueError:
    print("Please enter valid numbers for price and discount percentage.")
# Function to calculate the discounted price
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Apply discount only if it's 20% or more
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price  # Return original price if discount is less than 20%

# Prompt user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the result
print(f"Final price after discount: ${final_price:.2f}")

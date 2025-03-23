class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        # Initialize a list to hold the resulting words after processing
        processed_words = []
      
        # Split the sentence into words
        for word in sentence.split():
            # Check if the word is a price (starts with '$' and followed by digits)
            if word[0] == '$' and word[1:].isdigit():
                # If it is a price, calculate the new price after the discount
                original_price = int(word[1:])  # Remove the '$' sign and convert the rest to integer
                discounted_price = original_price * (1 - discount / 100)  # Apply discount
                word = f'${discounted_price:.2f}'  # Format the discounted price
              
            # Append the processed word to the list
            processed_words.append(word)
      
        # Join the processed words back into a sentence and return it
        return ' '.join(processed_words)
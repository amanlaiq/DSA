class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        processed_words = []

        for word in sentence.split():
            if word[0] == "$" and word[1:].isdigit():
                original_price = int(word[1:])
                discounted_price = original_price * (1 - discount/100)
                word = f'${discounted_price:.2f}'
            processed_words.append(word)

        return ' '.join(processed_words)

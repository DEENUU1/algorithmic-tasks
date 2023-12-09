class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(searchWord)

        products.sort()
        res = []

        prev = products
        for i in range(n):
            temp = []
            for product in prev:
                if len(product) > i and product[i] == searchWord[i]:
                    temp.append(product)

            prev = temp
            res.append(temp[:3])

        return res
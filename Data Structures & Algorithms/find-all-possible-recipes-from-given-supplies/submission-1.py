class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # I see this as:
        # Make all possible recipies fro current ignredients
        # add recipe results to ingredients
        # repeat until exhaustive

        # TIME: O(N^2)
        # TIME: O(N) + O(N^2) (if every recipe has n ingredients...)
        supplies = set(supplies)
        
        out = []


        for i in range(len(ingredients)):
            ings = ingredients[i]
            # all ingredients present:
            if len(supplies.intersection(ings)) == len(ings):
                supplies.add(recipes[i])
                out.append(recipes[i])
        
        
        return out

            

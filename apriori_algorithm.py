def apriori(casher, min_support):
    frequent_itemsets = {}

    # Frequent itemsets of size 1
    frequent_itemsets[1] = {}
    for items in casher:
        for item in items:
            if frozenset([item]) in frequent_itemsets[1]:
                frequent_itemsets[1][frozenset([item])] += 1
            else:
                frequent_itemsets[1][frozenset([item])] = 1

    # Frequent itemsets of size k > 1
    k = 2
    while bool(frequent_itemsets[k-1]):
        frequent_itemsets[k] = {}
        # Generate candidate itemsets of size k
        for itemset1 in frequent_itemsets[k-1]:
            for itemset2 in frequent_itemsets[k-1]:
                if len(itemset1.union(itemset2)) == k:
                    candidate_itemset = itemset1.union(itemset2)
                    # Check if the candidate itemset is frequent
                    count = 0
                    for items in casher:
                        if candidate_itemset.issubset(items):
                            count += 1
                    if count >= min_support:
                        frequent_itemsets[k][candidate_itemset] = count
        k += 1

    return frequent_itemsets


casher = [['apple', 'banana', 'cherry'], 
                ['banana', 'cherry', 'durian'], 
                ['apple', 'banana', 'durian'], 
                ['banana', 'durian', 'elderberry'], 
                ['cherry', 'banana', 'apple']]
                
min_support = 2


frequent_itemsets = apriori(casher, min_support)
for k, itemsets in frequent_itemsets.items():
    if k >= 1:
        print(f"Frequent itemsets of size {k}:")
        for itemset, support in itemsets.items():
            print(f"{set(itemset)}: {support}")

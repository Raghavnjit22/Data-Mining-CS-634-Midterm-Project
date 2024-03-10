{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data Mining Midterm Project"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Importing Libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np \n",
    "import pandas as pd\n",
    "import itertools\n",
    "from itertools import combinations"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Importing Datasets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You selected Grocery Store dataset\n"
     ]
    }
   ],
   "source": [
    "data=pd.read_csv(r'C:\\Akhil\\NJIT Courses\\Data Mining\\Grocery Store.csv')\n",
    "print('You selected Grocery Store dataset')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   milk bread biscuit cornflakes bournvita  jam maggi  tea coffee cock sugar\n",
      "0     t     t       t        NaN       NaN  NaN   NaN  NaN    NaN  NaN   NaN\n",
      "1     t     t       t          t       NaN  NaN   NaN  NaN    NaN  NaN   NaN\n",
      "2   NaN     t     NaN        NaN         t  NaN   NaN    t    NaN  NaN   NaN\n",
      "3     t     t     NaN        NaN       NaN    t     t  NaN    NaN  NaN   NaN\n",
      "4   NaN   NaN       t        NaN       NaN  NaN     t    t    NaN  NaN   NaN\n",
      "5   NaN     t     NaN        NaN         t  NaN   NaN    t    NaN  NaN   NaN\n",
      "6   NaN   NaN     NaN          t       NaN  NaN     t    t    NaN  NaN   NaN\n",
      "7   NaN     t       t        NaN       NaN  NaN     t    t    NaN  NaN   NaN\n",
      "8   NaN     t     NaN        NaN       NaN    t     t    t    NaN  NaN   NaN\n",
      "9     t     t     NaN        NaN       NaN  NaN   NaN  NaN    NaN  NaN   NaN\n",
      "10  NaN   NaN       t          t       NaN  NaN   NaN  NaN      t    t   NaN\n",
      "11  NaN   NaN       t          t       NaN  NaN   NaN  NaN      t    t   NaN\n",
      "12  NaN   NaN     NaN        NaN         t  NaN   NaN  NaN      t  NaN     t\n",
      "13  NaN     t     NaN        NaN       NaN  NaN   NaN  NaN      t    t   NaN\n",
      "14  NaN     t       t        NaN       NaN  NaN   NaN  NaN    NaN  NaN     t\n",
      "15  NaN   NaN     NaN          t       NaN  NaN   NaN  NaN      t  NaN     t\n",
      "16  NaN     t     NaN        NaN         t  NaN   NaN  NaN    NaN  NaN     t\n",
      "17  NaN     t     NaN        NaN       NaN  NaN   NaN  NaN      t  NaN     t\n",
      "18  NaN     t     NaN        NaN       NaN  NaN   NaN  NaN      t  NaN     t\n",
      "19    t   NaN     NaN          t       NaN  NaN   NaN    t      t  NaN   NaN\n"
     ]
    }
   ],
   "source": [
    "print(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  milk bread biscuit cornflakes bournvita  jam maggi  tea coffee cock sugar\n",
      "0    t     t       t        NaN       NaN  NaN   NaN  NaN    NaN  NaN   NaN\n",
      "1    t     t       t          t       NaN  NaN   NaN  NaN    NaN  NaN   NaN\n",
      "2  NaN     t     NaN        NaN         t  NaN   NaN    t    NaN  NaN   NaN\n",
      "3    t     t     NaN        NaN       NaN    t     t  NaN    NaN  NaN   NaN\n",
      "4  NaN   NaN       t        NaN       NaN  NaN     t    t    NaN  NaN   NaN\n"
     ]
    }
   ],
   "source": [
    "print(df.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Indexing Each Item from the header of the data file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'milk': 1,\n",
       " 'bread': 2,\n",
       " 'biscuit': 3,\n",
       " 'cornflakes': 4,\n",
       " 'bournvita': 5,\n",
       " 'jam': 6,\n",
       " 'maggi': 7,\n",
       " 'tea': 8,\n",
       " 'coffee': 9,\n",
       " 'cock': 10,\n",
       " 'sugar': 11}"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "item_list = list(df.columns)\n",
    "item_dict = dict()\n",
    "\n",
    "for i, item in enumerate(item_list):\n",
    "    item_dict[item] = i + 1\n",
    "\n",
    "item_dict"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Extracting Transactions from the Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "transactions = list()\n",
    "\n",
    "for i, row in df.iterrows():\n",
    "    transaction = set()\n",
    "    \n",
    "    for item in item_dict:\n",
    "        if row[item] == 't':\n",
    "            transaction.add(item_dict[item])\n",
    "    transactions.append(transaction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{1, 2, 3},\n",
       " {1, 2, 3, 4},\n",
       " {2, 5, 8},\n",
       " {1, 2, 6, 7},\n",
       " {3, 7, 8},\n",
       " {2, 5, 8},\n",
       " {4, 7, 8},\n",
       " {2, 3, 7, 8},\n",
       " {2, 6, 7, 8},\n",
       " {1, 2},\n",
       " {3, 4, 9, 10},\n",
       " {3, 4, 9, 10},\n",
       " {5, 9, 11},\n",
       " {2, 9, 10},\n",
       " {2, 3, 11},\n",
       " {4, 9, 11},\n",
       " {2, 5, 11},\n",
       " {2, 9, 11},\n",
       " {2, 9, 11},\n",
       " {1, 4, 8, 9}]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "transactions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Get Support Function that evaluates the support value for a set given all the transactions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_support(transactions, item_set):\n",
    "    match_count = 0\n",
    "    for transaction in transactions:\n",
    "        if item_set.issubset(transaction):\n",
    "            match_count += 1\n",
    "            \n",
    "    return float(match_count/len(transactions))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# self_join performs join based on the last level valid sets. It joins each sets together by performing union and if the length exceeds the current level, it will skip that set."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "metadata": {},
   "outputs": [],
   "source": [
    "def self_join(frequent_item_sets_per_level, level):\n",
    "    current_level_candidates = list()\n",
    "    last_level_items = frequent_item_sets_per_level[level - 1]\n",
    "    \n",
    "    if len(last_level_items) == 0:\n",
    "        return current_level_candidates\n",
    "    \n",
    "    for i in range(len(last_level_items)):\n",
    "        for j in range(i+1, len(last_level_items)):\n",
    "            itemset_i = last_level_items[i][0]\n",
    "            itemset_j = last_level_items[j][0]\n",
    "            union_set = itemset_i.union(itemset_j)\n",
    "            \n",
    "            if union_set not in current_level_candidates and len(union_set) == level:\n",
    "                current_level_candidates.append(union_set)\n",
    "                \n",
    "    return current_level_candidates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_single_drop_subsets(item_set):\n",
    "    single_drop_subsets = list()\n",
    "    for item in item_set:\n",
    "        temp = item_set.copy()\n",
    "        temp.remove(item)\n",
    "        single_drop_subsets.append(temp)\n",
    "        \n",
    "    return single_drop_subsets\n",
    "\n",
    "def is_valid_set(item_set, prev_level_sets):\n",
    "    single_drop_subsets = get_single_drop_subsets(item_set)\n",
    "    \n",
    "    for single_drop_set in single_drop_subsets:\n",
    "        if single_drop_set not in prev_level_sets:\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "def pruning(frequent_item_sets_per_level, level, candidate_set):\n",
    "    post_pruning_set = list()\n",
    "    if len(candidate_set) == 0:\n",
    "        return post_pruning_set\n",
    "    \n",
    "    prev_level_sets = list()\n",
    "    for item_set, _ in frequent_item_sets_per_level[level - 1]:\n",
    "        prev_level_sets.append(item_set)\n",
    "        \n",
    "    for item_set in candidate_set:\n",
    "        if is_valid_set(item_set, prev_level_sets):\n",
    "            post_pruning_set.append(item_set)\n",
    "            \n",
    "    return post_pruning_set"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# This is the main function which uses all the above described Utility functions to implement the Apriori Algorithm and generate the list of frequent itemsets for each level for the provided transactions and min_support value."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "metadata": {},
   "outputs": [],
   "source": [
    "from collections import defaultdict\n",
    "def apriori(min_support):\n",
    "    frequent_item_sets_per_level = defaultdict(list)\n",
    "    print(\"level : 1\", end = \" \")\n",
    "    \n",
    "    for item in range(1, len(item_list) + 1):\n",
    "        support = get_support(transactions, {item})\n",
    "        if support >= min_support:\n",
    "            frequent_item_sets_per_level[1].append(({item}, support))\n",
    "        \n",
    "    for level in range(2, len(item_list) + 1):\n",
    "        print(level, end = \" \")\n",
    "        current_level_candidates = self_join(frequent_item_sets_per_level, level)\n",
    "\n",
    "        post_pruning_candidates = pruning(frequent_item_sets_per_level, level, current_level_candidates)\n",
    "        if len(post_pruning_candidates) == 0:\n",
    "            break\n",
    "\n",
    "        for item_set in post_pruning_candidates:\n",
    "            support = get_support(transactions, item_set)\n",
    "            if support >= min_support:\n",
    "                frequent_item_sets_per_level[level].append((item_set, support))\n",
    "                \n",
    "    return frequent_item_sets_per_level"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Entering the Minimum Support Value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Minimum Support :  20\n",
      "level : 1 2 3 "
     ]
    }
   ],
   "source": [
    "print(\"Enter the Minimum Support : \")\n",
    "min_support = input()\n",
    "min_support = (min_support)/100\n",
    "frequent_item_sets_per_level = apriori(min_support)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# The below code produces a dictionary called item_support_dict which from frequent_item_sets_per_level that maps items to their support values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "metadata": {},
   "outputs": [],
   "source": [
    "item_support_dict = dict()\n",
    "item_list = list()\n",
    "\n",
    "key_list = list(item_dict.keys())\n",
    "val_list = list(item_dict.values())\n",
    "\n",
    "for level in frequent_item_sets_per_level:\n",
    "    for set_support_pair in frequent_item_sets_per_level[level]:\n",
    "        for i in set_support_pair[0]:\n",
    "            item_list.append(key_list[val_list.index(i)])\n",
    "        item_support_dict[frozenset(item_list)] = set_support_pair[1]\n",
    "        item_list = list()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# The find_subset function takes the item and item_length as parameter and it returns all the possible combinations of elements inside the items"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "metadata": {},
   "outputs": [],
   "source": [
    "def find_subset(item, item_length):\n",
    "    combs = []\n",
    "    for i in range(1, item_length + 1):\n",
    "        combs.append(list(combinations(item, i)))\n",
    "        \n",
    "    subsets = []\n",
    "    for comb in combs:\n",
    "        for elt in comb:\n",
    "            subsets.append(elt)\n",
    "            \n",
    "    return subsets"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# This function generates the association rules in accordance withe the minimum confidence value and the provided dictionary of itemsets against their support values. It takes the mininmum confidence value and support_dict as a parameter, and returns rules as a list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "metadata": {},
   "outputs": [],
   "source": [
    "def association_rules(min_confidence, support_dict):\n",
    "    rules = list()\n",
    "    for item, support in support_dict.items():\n",
    "        item_length = len(item)\n",
    "       \n",
    "        if item_length > 1:\n",
    "            subsets = find_subset(item, item_length)\n",
    "           \n",
    "            for A in subsets:\n",
    "                B = item.difference(A)\n",
    "               \n",
    "                if B:\n",
    "                    A = frozenset(A)\n",
    "                    \n",
    "                    AB = A | B\n",
    "                    \n",
    "                    confidence = support_dict[AB] / support_dict[A]\n",
    "                    if confidence >= min_confidence:\n",
    "                        rules.append((A, B, confidence))\n",
    "    \n",
    "    return rules"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Minimum Confidence :  30\n"
     ]
    }
   ],
   "source": [
    "print(\"Enter the Minimum Confidence : \")\n",
    "confidence = input()\n",
    "min_confidence = (confidence)/100\n",
    "association_rules = association_rules(min_confidence, support_dict = item_support_dict)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Output"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of rules:  14 \n",
      "\n",
      "{'milk'} -> {'bread'} <confidence: 0.8>\n",
      "{'bread'} -> {'milk'} <confidence: 0.3076923076923077>\n",
      "{'bread'} -> {'biscuit'} <confidence: 0.3076923076923077>\n",
      "{'biscuit'} -> {'bread'} <confidence: 0.5714285714285715>\n",
      "{'bread'} -> {'tea'} <confidence: 0.3076923076923077>\n",
      "{'tea'} -> {'bread'} <confidence: 0.5714285714285715>\n",
      "{'bread'} -> {'sugar'} <confidence: 0.3076923076923077>\n",
      "{'sugar'} -> {'bread'} <confidence: 0.6666666666666667>\n",
      "{'cornflakes'} -> {'coffee'} <confidence: 0.6666666666666667>\n",
      "{'coffee'} -> {'cornflakes'} <confidence: 0.5>\n",
      "{'maggi'} -> {'tea'} <confidence: 0.8>\n",
      "{'tea'} -> {'maggi'} <confidence: 0.5714285714285715>\n",
      "{'coffee'} -> {'sugar'} <confidence: 0.5>\n",
      "{'sugar'} -> {'coffee'} <confidence: 0.6666666666666667>\n"
     ]
    }
   ],
   "source": [
    "print(\"Number of rules: \", len(association_rules))\n",
    "\n",
    "for rule in association_rules:\n",
    "    print('{0} -> {1} <confidence: {2}>'.format(set(rule[0]), set(rule[1]), rule[2]))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

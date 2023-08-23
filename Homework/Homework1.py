{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ae12d25e-86b2-469b-881a-03f3cdfff13b",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "    Question 2: \n",
    "    find all unique elements in a list\n",
    "    l = [0,0,0,1,1,1,1,2,2,3,3,4]\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9a72006d-73ce-4e4a-95a0-d64e2437a1d2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3, 4]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l = [0,0,0,1,1,1,1,2,2,3,3,4]\n",
    "#l = [1,6,5,4,5,6,7,1,2,3,0,8,8,8,8,9]\n",
    "unique_list = []\n",
    "def unique(a):\n",
    "    for x in l:\n",
    "        if x not in unique_list:\n",
    "            unique_list.append(x)\n",
    "    return unique_list\n",
    "unique(l)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6fa7f4bc-1069-4e08-95cb-36c60bfd1531",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "    find sum of large numbers in the list\n",
    "    num1 = [1, 2]\n",
    "    num2 = [1, 9, 8, 1, 1, 1]\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f9ac0be3-60b2-4874-ab8e-9e99efefbff1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "num1 = [1, 2]\n",
    "num2 = [1, 9, 8, 1, 1, 1]\n",
    "\n",
    "def greatest_sum(list1, list2):\n",
    "    total = max(list1) + max(list2)\n",
    "    return total\n",
    "greatest_sum(num1, num2)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "22701e43-62b5-4fc4-b008-cb8d79d6f712",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "num1 = [1, 2]\n",
    "num2 = [1, 9, 8, 1, 1, 1]\n",
    "\n",
    "def lmax(list1):\n",
    "    max = list1[0]\n",
    "    for x in list1:\n",
    "        if x > max:\n",
    "            max = x\n",
    "    return max\n",
    "\n",
    "def sum(a,b):\n",
    "    return a + b\n",
    "sum(lmax(num1),lmax(num2))\n",
    "\n",
    "#print(sum((lmax(num1),(lmax(num2)))))\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "ec61bd50-998c-44f2-9258-3f4fb518abfa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\n    Q4: find if the given number is prime or not\\n'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"\n",
    "    Q4: find if the given number is prime or not\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "487269ed-9980-4471-b58d-142ea0dae9fa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a Number 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7 is a prime number\n"
     ]
    }
   ],
   "source": [
    "a= int(input(\"Enter a Number\"))\n",
    "i=2\n",
    "flag=0\n",
    "while i <=(a/2):\n",
    "    if a%i==0:\n",
    "        flag = 1\n",
    "        break\n",
    "    i=i+1\n",
    "if flag==1:\n",
    "    print(f\"{a} is not a prime number\")\n",
    "else:\n",
    "    print(f\"{a} is a prime number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ebaf6e93-7159-4b41-89a8-3aca88a95f8e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a54a5c7-4720-41c3-b82c-50ed92fbf047",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

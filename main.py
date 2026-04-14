# 11. Matnda nechta unli bor
s = input()
vowels = "aeiou"
print(sum(1 for c in s if c.lower() in vowels))

# 12. Listni teskarisiga o‘girish
lst = list(map(int, input().split()))
print(lst[::-1])

# 13. Ikki listni birlashtirish
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(a + b)

# 14. Eng uzun so‘zni topish
words = input().split()
print(max(words, key=len))

# 15. Takrorlanmagan elementlar
lst = list(map(int, input().split()))
print(list(set(lst)))

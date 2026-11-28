
# apl-source:1
# مثال 887 — متتابعة هوفشتاتر Q
# apl-source:2
# Hofstadter Q-sequence
# apl-source:3
# Demonstrates: استدعاء ذاتي متداخل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/887-hofstadter-q.apl
# apl-source:6

# apl-source:7
# متتابعة هوفشتاتر Q: Q(n) = Q(n-Q(n-1)) + Q(n-Q(n-2))
# apl-source:8
# تكرارية "فوضوية" تبدو عشوائية لكنها معرفة بدقة
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
def هوفشتاتر(ن):
  # apl-source:19
  ق = [0, 1, 1]
  # apl-source:20
  for i in range(3, ن + 1):
    # apl-source:21
    ق = ق + [ق[i - ق[i - 1]] + ق[i - ق[i - 2]]]
  # apl-source:22
  return ق
# apl-source:23

# apl-source:24
ق = هوفشتاتر(10)
# apl-source:25
print("Q1..Q10:", ق[1:])
# apl-source:26

# apl-source:27
تأكد_يساوي(ق[1], 1, "Q(1) = 1")
# apl-source:28
تأكد_يساوي(ق[3], 2, "Q(3) = 2")
# apl-source:29
تأكد_يساوي(ق[5], 3, "Q(5) = 3")
# apl-source:30
تأكد_يساوي(ق[7], 5, "Q(7) = 5")
# apl-source:31
تأكد_يساوي(ق[10], 6, "Q(10) = 6")
# apl-source:32

# apl-source:33
# Q(n) <= n دائماً للنطاق المحسوب
# apl-source:34
ق50 = هوفشتاتر(50)
# apl-source:35
for i in range(1, 51):
  # apl-source:36
  تأكد_يساوي(ق50[i] <= i, 1 == 1, "Q <= n عند " + str(i))
# apl-source:37

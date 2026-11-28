
# apl-source:1
# مثال 861 — أعداد لوكاس
# apl-source:2
# Lucas numbers
# apl-source:3
# Demonstrates: تبدأ 2,1 بنفس التكرارية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/861-lucas-numbers.apl
# apl-source:6

# apl-source:7
# أعداد لوكاس: مثل فيبوناتشي لكنها تبدأ 2, 1
# apl-source:8
# L(n) = L(n-1) + L(n-2) وترتبط بالنسبة الذهبية
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
def لوكاس(ن):
  # apl-source:19
  أ = 2
  # apl-source:20
  ب = 1
  # apl-source:21
  for _ in range(ن):
    # apl-source:22
    جديد = أ + ب
    # apl-source:23
    أ = ب
    # apl-source:24
    ب = جديد
  # apl-source:25
  return أ
# apl-source:26

# apl-source:27
أول_عشرة = []
# apl-source:28
for i in range(10):
  # apl-source:29
  أول_عشرة = أول_عشرة + [لوكاس(i)]
# apl-source:30
print("L0..L9:", أول_عشرة)
# apl-source:31

# apl-source:32
تأكد_يساوي(لوكاس(0), 2, "L0 = 2")
# apl-source:33
تأكد_يساوي(لوكاس(1), 1, "L1 = 1")
# apl-source:34
تأكد_يساوي(لوكاس(5), 11, "L5 = 11")
# apl-source:35
تأكد_يساوي(لوكاس(10), 123, "L10 = 123")
# apl-source:36

# apl-source:37
# هوية: L(n) = F(n-1) + F(n+1)
# apl-source:38
def فيب(ن):
  # apl-source:39
  أ = 0
  # apl-source:40
  ب = 1
  # apl-source:41
  for _ in range(ن):
    # apl-source:42
    جديد = أ + ب
    # apl-source:43
    أ = ب
    # apl-source:44
    ب = جديد
  # apl-source:45
  return أ
# apl-source:46

# apl-source:47
تأكد_يساوي(لوكاس(7), فيب(6) + فيب(8), "L(n) = F(n-1)+F(n+1)")
# apl-source:48

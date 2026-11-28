
# apl-source:1
# مثال 2054 — تكافؤ عدد البتات بطي XOR
# apl-source:2
# Bit parity by XOR folding
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2054-parity-of-bits-xor-fold.apl
# apl-source:6

# apl-source:7
# # نطبق XOR مع الإزاحة 16 ثم 8 ثم 4 ثم 2 ثم 1
# apl-source:8
# # آخر بت هو التكافؤ
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
def تكافؤ(ن):
  # apl-source:19
  for ز in [16, 8, 4, 2, 1]:
    # apl-source:20
    ن = ن ^ (ن >> ز)
  # apl-source:21
  return ن & 1
# apl-source:22

# apl-source:23
تأكد_يساوي(تكافؤ(7), 1, "٧")
# apl-source:24
تأكد_يساوي(تكافؤ(8), 1, "٨")
# apl-source:25
تأكد_يساوي(تكافؤ(3), 0, "٣")
# apl-source:26
تأكد_يساوي(تكافؤ(0), 0, "صفر")
# apl-source:27
تأكد_يساوي(تكافؤ(255), 0, "٢٥٥")
# apl-source:28

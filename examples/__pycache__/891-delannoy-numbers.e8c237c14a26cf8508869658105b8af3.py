
# apl-source:1
# مثال 891 — أعداد ديلانواي
# apl-source:2
# Delannoy numbers
# apl-source:3
# Demonstrates: شبكة بخطوة قطرية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/891-delannoy-numbers.apl
# apl-source:6

# apl-source:7
# أعداد ديلانواي: مسارات الشبكة بخطوات يمين/أعلى/قطر
# apl-source:8
# D(i,j) = D(i-1,j) + D(i,j-1) + D(i-1,j-1)
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
def ديلانواي(صفوف, أعمدة):
  # apl-source:19
  د = []
  # apl-source:20
  for _ in range(صفوف + 1):
    # apl-source:21
    صف = []
    # apl-source:22
    for __ in range(أعمدة + 1):
      # apl-source:23
      صف = صف + [1]
    # apl-source:24
    د = د + [صف]
  # apl-source:25
  for i in range(1, صفوف + 1):
    # apl-source:26
    for ج in range(1, أعمدة + 1):
      # apl-source:27
      د[i][ج] = د[i - 1][ج] + د[i][ج - 1] + د[i - 1][ج - 1]
  # apl-source:28
  return د[صفوف][أعمدة]
# apl-source:29

# apl-source:30
print("D(2,2) =", ديلانواي(2, 2))
# apl-source:31
print("D(3,3) =", ديلانواي(3, 3))
# apl-source:32
print("D(3,5) =", ديلانواي(3, 5))
# apl-source:33

# apl-source:34
تأكد_يساوي(ديلانواي(0, 0), 1, "الأصل مسار واحد")
# apl-source:35
تأكد_يساوي(ديلانواي(2, 2), 13, "D(2,2) = 13")
# apl-source:36
تأكد_يساوي(ديلانواي(3, 3), 63, "D(3,3) = 63")
# apl-source:37
تأكد_يساوي(ديلانواي(3, 5), 231, "D(3,5) = 231")
# apl-source:38

# apl-source:39
# تماثل: D(i,j) = D(j,i)
# apl-source:40
تأكد_يساوي(ديلانواي(5, 3), 231, "التماثل D(5,3)")
# apl-source:41

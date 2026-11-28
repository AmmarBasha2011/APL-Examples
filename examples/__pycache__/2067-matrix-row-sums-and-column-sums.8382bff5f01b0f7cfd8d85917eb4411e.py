
# apl-source:1
# مثال 2067 — مجاميع صفوف وأعمدة المصفوفة
# apl-source:2
# Row and column sums
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2067-matrix-row-sums-and-column-sums.apl
# apl-source:6

# apl-source:7
# # نجمع كل صف ثم كل عمود
# apl-source:8
# # في مرور واحد
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
def مجاميع(م):
  # apl-source:19
  صفوف = []
  # apl-source:20
  اعمدة = [0] * len(م[0])
  # apl-source:21
  for صف in م:
    # apl-source:22
    مج = 0
    # apl-source:23
    for ك in range(len(صف)):
      # apl-source:24
      مج = مج + صف[ك]
      # apl-source:25
      اعمدة[ك] = اعمدة[ك] + صف[ك]
    # apl-source:26
    صفوف = صفوف + [مج]
  # apl-source:27
  return [صفوف, اعمدة]
# apl-source:28

# apl-source:29
تأكد_يساوي(مجاميع([[1, 2], [3, 4], [5, 6]]), [[3, 7, 11], [9, 12]], "٣×٢")
# apl-source:30
تأكد_يساوي(مجاميع([[5]]), [[5], [5]], "واحد")
# apl-source:31

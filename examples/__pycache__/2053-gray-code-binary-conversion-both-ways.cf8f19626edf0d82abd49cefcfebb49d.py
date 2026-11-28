
# apl-source:1
# مثال 2053 — تحويل بين الثنائي ورمز غراي
# apl-source:2
# Binary and Gray code conversion
# apl-source:3
# Demonstrates: بتات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2053-gray-code-binary-conversion-both-ways.apl
# apl-source:6

# apl-source:7
# # التحويل إلى غراي خطوة واحدة
# apl-source:8
# # والعكس نكرر XOR مع الإزاحات
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
def الى_غراي(ن):
  # apl-source:19
  return ن ^ (ن >> 1)
# apl-source:20

# apl-source:21
def من_غراي(غ):
  # apl-source:22
  ناتج = غ
  # apl-source:23
  غ = غ >> 1
  # apl-source:24
  while غ > 0:
    # apl-source:25
    ناتج = ناتج ^ غ
    # apl-source:26
    غ = غ >> 1
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
قائمة = []
# apl-source:30
for ك in range(8):
  # apl-source:31
  قائمة = قائمة + [الى_غراي(ك)]
# apl-source:32
تأكد_يساوي(قائمة, [0, 1, 3, 2, 6, 7, 5, 4], "ثمانية")
# apl-source:33
تأكد_يساوي(من_غراي(6), 4, "٦")
# apl-source:34
تأكد_يساوي(من_غراي(7), 5, "٧")
# apl-source:35
تأكد_يساوي(من_غراي(الى_غراي(1234)), 1234, "ذهاب وإياب")
# apl-source:36

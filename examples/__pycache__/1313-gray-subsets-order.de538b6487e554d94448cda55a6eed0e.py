
# apl-source:1
# مثال 1313 — ترتيب مجموعات غراي
# apl-source:2
# Subsets in gray code order
# apl-source:3
# Demonstrates: شيفرة غراي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1313-gray-subsets-order.apl
# apl-source:6

# apl-source:7
# نستخدم شيفرة غراي كقناع
# apl-source:8
# فيتغير عنصر واحد بين كل مجموعتين متجاورتين
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
def مجموعات_غراي(أ):
  # apl-source:19
  ناتج = []
  # apl-source:20
  for ع in range(1 << len(أ)):
    # apl-source:21
    قناع = ع ^ (ع >> 1)
    # apl-source:22
    ق = []
    # apl-source:23
    for ب in range(len(أ)):
      # apl-source:24
      if (قناع >> ب) & 1:
        # apl-source:25
        ق = ق + [أ[ب]]
    # apl-source:26
    ناتج = ناتج + [ق]
  # apl-source:27
  return ناتج
# apl-source:28

# apl-source:29
def فرق(أ, ب):
  # apl-source:30
  ع = 0
  # apl-source:31
  for س in أ:
    # apl-source:32
    if س not in ب:
      # apl-source:33
      ع = ع + 1
  # apl-source:34
  for س in ب:
    # apl-source:35
    if س not in أ:
      # apl-source:36
      ع = ع + 1
  # apl-source:37
  return ع
# apl-source:38

# apl-source:39
ق = مجموعات_غراي([1, 2, 3])
# apl-source:40
تأكد_يساوي(len(ق), 8, "ثماني مجموعات")
# apl-source:41
سليم = True
# apl-source:42
for ع in range(7):
  # apl-source:43
  if فرق(ق[ع], ق[ع + 1]) != 1:
    # apl-source:44
    سليم = False
# apl-source:45
تأكد_يساوي(سليم, True, "فرق عنصر واحد")
# apl-source:46

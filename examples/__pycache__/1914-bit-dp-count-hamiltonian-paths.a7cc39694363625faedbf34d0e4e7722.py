
# apl-source:1
# مثال 1914 — عدد المسارات الهاميلتونية بالبتات
# apl-source:2
# Count Hamiltonian paths with bit masks
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1914-bit-dp-count-hamiltonian-paths.apl
# apl-source:6

# apl-source:7
# حالة = قناع وآخر عقدة
# apl-source:8
# نمدد المسار بعقدة غير مزارة
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
def مسارات(ن, حواف):
  # apl-source:19
  كل = (1 << ن) - 1
  # apl-source:20
  جدول = []
  # apl-source:21
  for م in range(كل + 1):
    # apl-source:22
    صف = []
    # apl-source:23
    for ع in range(ن):
      # apl-source:24
      صف = صف + [0]
    # apl-source:25
    جدول = جدول + [صف]
  # apl-source:26
  for ع in range(ن):
    # apl-source:27
    جدول[1 << ع][ع] = 1
  # apl-source:28
  for م in range(كل + 1):
    # apl-source:29
    for ع in range(ن):
      # apl-source:30
      if جدول[م][ع] > 0:
        # apl-source:31
        for ت in range(ن):
          # apl-source:32
          if (م & (1 << ت)) == 0 and حواف[ع][ت] == 1:
            # apl-source:33
            جدول[م | (1 << ت)][ت] = جدول[م | (1 << ت)][ت] + جدول[م][ع]
  # apl-source:34
  كلي = 0
  # apl-source:35
  for ع in range(ن):
    # apl-source:36
    كلي = كلي + جدول[كل][ع]
  # apl-source:37
  return كلي
# apl-source:38

# apl-source:39
مثلث = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
# apl-source:40
خط = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
# apl-source:41
تأكد_يساوي(مسارات(3, مثلث), 6, "مثلث")
# apl-source:42
تأكد_يساوي(مسارات(3, خط), 2, "خط")
# apl-source:43

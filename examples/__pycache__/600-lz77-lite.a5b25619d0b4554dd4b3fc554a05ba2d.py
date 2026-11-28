
# apl-source:1
# مثال 600 — ضغط LZ77 المبسط
# apl-source:2
# LZ77 lite compression
# apl-source:3
# Demonstrates: ضغط، نافذة منزلقة، أزواج إزاحة وطول
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/600-lz77-lite.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# ضغط LZ77 المبسط: أزواج (إزاحة، طول، حرف)
# apl-source:25
# Demonstrates: نافذة منزلقة للضغط, فك الضغط, مكسب الحجم
# apl-source:26
# أساس ضغط zip و gzip
# apl-source:27

# apl-source:28
def اضغط(نص):
  # apl-source:29
  أزواج = []
  # apl-source:30
  ي = 0
  # apl-source:31
  while ي < len(نص):
    # apl-source:32
    أفضل_إزاحة = 0
    # apl-source:33
    أفضل_طول = 0
    # apl-source:34
    بداية = max(0, ي - 6)
    # apl-source:35
    for ج in range(بداية, ي):
      # apl-source:36
      ط = 0
      # apl-source:37
      while ي + ط < len(نص) and نص[ج + ط] == نص[ي + ط] and ط < 6:
        # apl-source:38
        ط = ط + 1
      # apl-source:39
      if ط > أفضل_طول:
        # apl-source:40
        أفضل_طول = ط
        # apl-source:41
        أفضل_إزاحة = ي - ج
    # apl-source:42
    if أفضل_طول >= 2:
      # apl-source:43
      أزواج.append([أفضل_إزاحة, أفضل_طول, ""])
      # apl-source:44
      ي = ي + أفضل_طول
    # apl-source:45
    else:
      # apl-source:46
      أزواج.append([0, 0, نص[ي]])
      # apl-source:47
      ي = ي + 1
  # apl-source:48
  return أزواج
# apl-source:49

# apl-source:50
def فك(أزواج):
  # apl-source:51
  ناتج = ""
  # apl-source:52
  for زوج in أزواج:
    # apl-source:53
    if زوج[0] == 0:
      # apl-source:54
      ناتج = ناتج + زوج[2]
    # apl-source:55
    else:
      # apl-source:56
      بداية = len(ناتج) - زوج[0]
      # apl-source:57
      for ك in range(زوج[1]):
        # apl-source:58
        ناتج = ناتج + ناتج[بداية + ك]
  # apl-source:59
  return ناتج
# apl-source:60

# apl-source:61
نص = "ababababab"
# apl-source:62
مضغوط = اضغط(نص)
# apl-source:63
print("أزواج:", مضغوط)
# apl-source:64
تأكد_يساوي(فك(مضغوط), نص, "فك الضغط يعيد الأصل")
# apl-source:65
تأكد_يساوي(len(مضغوط) < len(نص), True, "الضغط يقلص التكرار")
# apl-source:66
تأكد_يساوي(فك(اضغط("مرحبا")), "مرحبا", "نص بلا تكرار")
# apl-source:67

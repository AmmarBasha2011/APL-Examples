
# apl-source:1
# مثال 752 — عنقودات الإيموجي
# apl-source:2
# Emoji grapheme clusters
# apl-source:3
# Demonstrates: ZWJ، معدلات بشرة، محددات تنويع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/752-emoji-grapheme-split.apl
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
# تقسيم نص إلى عنقودات مرئية (grapheme clusters) للإيموجي
# apl-source:25
# Demonstrates: نقطة ترميز ZWJ, معدّلات لون البشرة, محددات التنويع
# apl-source:26
# العائلة 👨‍👩‍👧‍👦 عنقود واحد رغم أنها 7 نقاط ترميز
# apl-source:27

# apl-source:28
def هو_ممدد(نقطة):
  # apl-source:29
  if نقطة == 8205:
    # apl-source:30
    return True
  # apl-source:31
  if نقطة >= 127995 and نقطة <= 127999:
    # apl-source:32
    return True
  # apl-source:33
  if نقطة >= 65024 and نقطة <= 65039:
    # apl-source:34
    return True
  # apl-source:35
  return False
# apl-source:36

# apl-source:37
def عنقودات(نص):
  # apl-source:38
  ناتج = []
  # apl-source:39
  for ي in range(len(نص)):
    # apl-source:40
    نقطة = ord(نص[ي])
    # apl-source:41
    if len(ناتج) > 0 and هو_ممدد(نقطة):
      # apl-source:42
      ناتج[len(ناتج) - 1] = ناتج[len(ناتج) - 1] + نص[ي]
    # apl-source:43
    elif len(ناتج) > 0 and ناتج[len(ناتج) - 1].endswith("‍"):
      # apl-source:44
      ناتج[len(ناتج) - 1] = ناتج[len(ناتج) - 1] + نص[ي]
    # apl-source:45
    else:
      # apl-source:46
      ناتج.append(نص[ي])
  # apl-source:47
  return ناتج
# apl-source:48

# apl-source:49
أسرة = "👨‍👩‍👧‍👦"
# apl-source:50
عنقودات1 = عنقودات("👨‍👩‍👧‍👦👍🏽a❤️")
# apl-source:51

# apl-source:52
تأكد_يساوي(len(عنقودات1), 4, "أربعة عنقودات")
# apl-source:53
تأكد_يساوي(عنقودات1[0], "👨‍👩‍👧‍👦", "العائلة عنقود واحد")
# apl-source:54
تأكد_يساوي(عنقودات1[1], "👍🏽", "إبهام بلون بشرة")
# apl-source:55
تأكد_يساوي(عنقودات1[2], "a", "حرف لاتيني")
# apl-source:56
تأكد_يساوي(عنقودات1[3], "❤️", "قلب بمحدد تنويع")
# apl-source:57

# apl-source:58
تأكد_يساوي(len(عنقودات("abc")), 3, "نص عادي")
# apl-source:59
تأكد_يساوي(len(عنقودات("")), 0, "نص فارغ")
# apl-source:60
تأكد_يساوي(len(عنقودات("a👨‍👩‍👧‍👦b")), 3, "عائلة بين حرفين")
# apl-source:61
تأكد_يساوي(len(أسرة), 7, "سبع نقاط ترميز خام")
# apl-source:62

# apl-source:63
print("العنقودات:", عنقودات1)
# apl-source:64

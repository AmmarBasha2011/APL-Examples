
# apl-source:1
# مثال 1951 — سلم الكلمات: أقصر تحويل
# apl-source:2
# Word ladder shortest length
# apl-source:3
# Demonstrates: رسوم بيانية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1951-word-ladder-shortest-length-bfs.apl
# apl-source:6

# apl-source:7
# # نغير حرفا واحدا في كل خطوة بشرط وجود الكلمة في القاموس
# apl-source:8
# # ونعد عدد الكلمات في أقصر سلسلة
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
def سلم(بداية, نهاية, قاموس):
  # apl-source:19
  مسموح = {}
  # apl-source:20
  for ك in قاموس:
    # apl-source:21
    مسموح[ك] = 1
  # apl-source:22
  if (نهاية in مسموح) == False:
    # apl-source:23
    return 0
  # apl-source:24
  رأينا = {}
  # apl-source:25
  رأينا[بداية] = 1
  # apl-source:26
  طابور = [[بداية, 1]]
  # apl-source:27
  حروف = "abcdefghijklmnopqrstuvwxyz"
  # apl-source:28
  while len(طابور) > 0:
    # apl-source:29
    ح = طابور.pop(0)
    # apl-source:30
    if ح[0] == نهاية:
      # apl-source:31
      return ح[1]
    # apl-source:32
    for م in range(len(ح[0])):
      # apl-source:33
      for ر in حروف:
        # apl-source:34
        جديد = ح[0][:م] + ر + ح[0][م + 1:]
        # apl-source:35
        if (جديد in مسموح) and ((جديد in رأينا) == False):
          # apl-source:36
          رأينا[جديد] = 1
          # apl-source:37
          طابور = طابور + [[جديد, ح[1] + 1]]
  # apl-source:38
  return 0
# apl-source:39

# apl-source:40
ق = ["hot", "dot", "dog", "lot", "log", "cog"]
# apl-source:41
تأكد_يساوي(سلم("hit", "cog", ق), 5, "ممكن")
# apl-source:42
تأكد_يساوي(سلم("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0, "مستحيل")
# apl-source:43

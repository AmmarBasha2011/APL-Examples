
# apl-source:1
# مثال 656 — التعمق التكراري
# apl-source:2
# Iterative deepening
# apl-source:3
# Demonstrates: تعمق تكراري، حد عمق، بحث
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/656-iterative-deepening.apl
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
# التعمق التكراري: BFS بذاكرة DFS
# apl-source:25
# Demonstrates: حد عمق متزايد, بحث محدود العمق, أول حل أضحل
# apl-source:26
# يجد أقصر عمق بذاكرة شجرة البحث العميق
# apl-source:27

# apl-source:28
شجرة = {"أ": ["ب", "ج"], "ب": ["د", "ه"], "ج": ["و"], "د": [], "ه": ["ز"], "و": [], "ز": []}
# apl-source:29

# apl-source:30
def بحث_محدود(عقدة_حالية, هدف, حد, عمق):
  # apl-source:31
  if عقدة_حالية == هدف:
    # apl-source:32
    return عمق
  # apl-source:33
  if عمق == حد:
    # apl-source:34
    return -1
  # apl-source:35
  for فرع in شجرة[عقدة_حالية]:
    # apl-source:36
    ن = بحث_محدود(فرع, هدف, حد, عمق + 1)
    # apl-source:37
    if ن != -1:
      # apl-source:38
      return ن
  # apl-source:39
  return -1
# apl-source:40

# apl-source:41
def تعمق_تكراري(جذر, هدف, أقصى):
  # apl-source:42
  for حد in range(أقصى + 1):
    # apl-source:43
    ن = بحث_محدود(جذر, هدف, حد, 0)
    # apl-source:44
    if ن != -1:
      # apl-source:45
      return [حد, ن]
  # apl-source:46
  return [-1, -1]
# apl-source:47

# apl-source:48
تأكد_يساوي(تعمق_تكراري("أ", "ز", 5), [3, 3], "ز عند العمق الثالث")
# apl-source:49
تأكد_يساوي(تعمق_تكراري("أ", "و", 5), [2, 2], "و عند العمق الثاني")
# apl-source:50
تأكد_يساوي(تعمق_تكراري("أ", "أ", 5), [0, 0], "الجذر نفسه")
# apl-source:51
تأكد_يساوي(تعمق_تكراري("أ", "ز", 2), [-1, -1], "أقصى قليل لا يكفي")
# apl-source:52
تأكد_يساوي(بحث_محدود("أ", "ز", 2, 0), -1, "حد اثنان لا يصل")
# apl-source:53
print("انتهى التعمق")
# apl-source:54

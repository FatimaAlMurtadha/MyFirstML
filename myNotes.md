mkdir mtProject
cd myProject
git init 
touch .gitignore

# Start Python project
python -m venv .venv 

# ADD .venv to .gitignore

# ACTIVATE THE ENV
./.venv/Scripts/activate
## Or
source ./.venv/bin/activate

python --version

# install pip
pip install pandas numpy

# Option
pip3 install -r requirements.txt
pip3 freeze >requirements.txt

# Run
py scr/main.py OR WHAT EVER IS THE PATH

# Tests
pip install pytets

# Run the tests
python -m pytest -v

########################################################################################
------------------------------- ################## -------------------------------------

## DAY 2
- lambda function
x = lambda a, b: a * b
print(x(5, 6)) # 30

- It can be inside onther function
a function which return another function:

def curry(x, y)
    if x<= 0
      return lambda z: z*y
    return lambda _: x + y

- Lambda functions are commonly used with built-in functions like:
           map(), filter(), and sorted().


########################################################################################
------------------------------- ################## -------------------------------------

### YouTube course
# Containers (Lists , Tiuples, Dictionaries, Sets)

## 1) Lists []
- Lists: ordered, mutable, allows duplicates elements / many data types are available
- If I have a copy of a list and then I modivied it THIS will modify the original one
- index [1] OR [-1]
- index out of bound [100] Error
- change by index
- print with for loop
- if in the tuple
- len
- myTuple.count('t')
- myTuple.index('t')
- Change to a list my_list = list(myTuple)
- myTuple2 = tuple(my_list)
- Slice [1:4] the right is not count
- [:] all
- [::2] every second element
- [::-1] Reversing
- slicing out of bount [100:200] will give an empty list []
- # Methods with lists:
- a) my_list.append(my_list2) -> add to the end as a block
- b) my_list.extend(my_list2) -> add to the end indiviually element by element
- c) my_list.pop(2) -> Remove the item on index 2
- d) my_list.pop() -> will only remove the last element
- e) my_list.reverse()
- f) my_list.count("t") how many times does letter T occur

========================================  LIST COMPREHENSION =============================

we create a new list based on the values of an existing list
numbers = [1,2,3,4,5,6,7,8,9,10,11,12]

new_numbers_list = [n*2 for n in numbers if 1 <= n <= 3]
- will gives us [2, 4,6] 


# 2) Tuples () or w/o
- Tuple: ordered, immutable, allows duplicate elements
- index + Slice === Lists
- change by index  --------  my_tuple[0] = 5 -- ERROR
- one element ==> (1) is onnly int while (1,) is a tuple
- print with for loop
- if in the tuple
- len
- myTuple.count('t')
- myTuple.index('t')
- Change to a list my_list = list(myTuple)
- myTuple2 = tuple(my_list)
- Every element separetly

print("="*4, ""*2, " Every elemnt seperatly  ","="*4, ""*2)
print()
name, age , city = myTuple
print(name)
print(age)
print(city)

# 3) Dictionaries: key-Value pairs, Unordered, Immutable NO index but Key
- new dic w/o quates
- Access with a value 
- Add new key-value items
- del // To delete by key ---- del mydiction["name"]
- mydiction.pop("age")
- Delete the last item ------- mydiction.popitem()
- if "name" in mydiction
- try: ..... except: .....
- for key in mydiction
- for key in mydiction.key() ----- The same
- for value in mydition.value()
- for key, value in mydition.items()
- mydiction_cpy = mydiction
- if I modify the copy this will modify the original one
- To avoid that ------------ mydiction_cpy = mydiction.copy() -- OR -- mydiction_cpy = dict(mydiction)
- Merge  ---------- mydition.update(mydiction2)

# 4) Set: Unordered, No duplicate elements {} set([])
- set_1 = {"apple", "apple", "apple", "banana", "banana"}
- set_2 = set(["banana", "apple"])
- print(set_1 == set_2) # True // NO DUPLICATE
- union BOTH w/o duplicate
- intersection    the shared elements
- difference IN ONE BUT NOT ON THE OTHER
- Can't create an empty set

============================= Converion ===============================
============================= Iteration & Loops ===============================
============================= The range function ===============================

- range(start, stop, step)
- range(4) is equlvalent to range(0,4,1)
- range(5, 10) is equlvalent to range(5, 10, 1)

======================= The enumerate function RECOMMENDED insteade of using range ===============================

================= A double for-loop ===============
for inside another for

============== While loop =============

============== Functions =============

============== Restriction Functions =============

- kwargs_only(*,arg1, arg2) ----- Must write arg1= 1, arg2 =3
- pos_only(arg1, arg2, /) ----- Must write the postion only

============== Unpacking =============
- sum_three_numbers(*my_tuple)
- sum_three_numbers(**my_dection)

============== Variable Number of Arguments =============
- sum_numbers(*args) // as many as I want
- sum_number(**kwargs)

########################################################################################
------------------------------- Classes -------------------------------------
- instance, attributes, methods, inheritance
- 







########################################################################################
------------------------------- Exeptions -------------------------------------
- catcting, build-in eceptions, else, finally, raising


########################################################################################
------------------------------- Numpy -------------------------------------
- arraies operations, learn-more
- Vi behöver en tom array [[...columns...],[...rows...]] ==> [[0], [0]]
- Game of life
- en array numpy är snabbare än en lista -- mycket prestanda
- ## Vad är formen och Vad är typen
- they should have balance -- same count of variables or cells
- vi bearbeta data parallelt tvärtom listor som går en per en
- # Broadcasting: 
- # Form: the same monster should be on all the data or forms that we have
- # data type : We can't mix data types here as we do in the usuall arraies
- 





########################################################################################
------------------------------- Matplotlib -------------------------------------

- Plot, types, advanced, subplots and different plot types, more







########################################################################################
------------------------------- Pandas -------------------------------------
- inpecting our data, sorting, inplace opersions, selecting data, missing data, plotting data, more

# Pandas DF
####  Drop missing data: df = df.dropna()
df

- Condition: df = df.dropna(how='all') // df = df.dropna(subset=['gender'])

#### Fill missing data
- df = df.fillna(value=['Not Found'])
- df = df.fillna(['year': 0,'category': 'Unknown'])
- df = df.
- df = df.
- df = df.


########################################################################################
------------------------------- ################## -------------------------------------
# student_performence_final_score.csv
1- Correlation Heatmap ( Student Performance Final Score)  كيف يمكن استخدام هذه النتائج في Lexaura؟

Lexaura يمكنها أن تصبح مستشارة دراسية ذكية:

- إذا كان الطالب يدرس قليلًا → تقترح زيادة ساعات الدراسة  
- إذا كان لديه قلق امتحاني → تقدم تمارين تهدئة  
- إذا كان لديه Stress عالي → تقدم خطة إدارة ضغط  
- إذا كان Previous_GPA منخفض → تقترح Tutoring  
- إذا كان Screen_Time مرتفع → تقترح تقليل الاستخدام قبل الامتحانات

# DATA STORYTELLING ( Hours studied vs Final score)
🚀 6. كيف يخدم هذا Lexaura؟

هذا الرسم يعطي Lexaura القدرة على:

- تقديم توصيات شخصية للطلاب  
- تحديد الحد الأدنى من ساعات الدراسة للوصول إلى هدف معين  
- اكتشاف الطلاب الذين يدرسون كثيرًا لكن نتائجهم منخفضة (علامة خطر)  
- تقديم نصائح لتحسين الأداء بناءً على السلوك الدراسي  

مثال:  
> “Based on your current study hours, your expected score is around 72.  
> To reach 85, you need to increase your study time by 2–3 hours per day.”

هذا هو جوهر Lexaura.

# DATA STORYTELLING ( Exam anxiety vs Final score)
🚀 5. كيف يخدم هذا Lexaura؟

هذا الرسم يعطي Lexaura القدرة على:

- اكتشاف الطلاب المعرضين لخطر الأداء المنخفض  
- تقديم توصيات نفسية وسلوكية  
- اقتراح تمارين تنفس أو إدارة قلق  
- تعديل خطة الدراسة بناءً على الحالة النفسية  
- التنبؤ بالنتائج بدقة أعلى عبر دمج العوامل النفسية  

مثال على توصية ذكية داخل Lexaura:

> “Your anxiety level is high. Even with good study hours, your expected score may drop.  
> Try reducing anxiety by 2 points to improve your predicted score by ~10 points.”

هذا هو الذكاء الحقيقي الذي يميز Lexaura.

# DATA STORYTELLING ( Distribution of final score ) - The level of difficulty of the educational system and the performance of the students as a whole

🚀 5. كيف يخدم هذا Lexaura؟

هذا الرسم يعطي Lexaura القدرة على:

- تحديد مستوى صعوبة الاختبارات  
- معرفة ما إذا كان الطالب “خارج النمط” (Outlier)  
- تقديم توصيات بناءً على موقع الطالب في التوزيع  
- اكتشاف الطلاب الذين يحتاجون دعمًا إضافيًا  
- مقارنة أداء الطالب بالمجموعة (Benchmarking)

مثال توصية ذكية داخل Lexaura:

> “Your score is 72, which is below the group’s main cluster (80–100).  
> Increasing study hours by 2–3 hours per day could move you into the high‑performance range.”

# DATA STORYTELLING ( Final score by study method "Online , Offline , Hybrid")
🚀 5. كيف يخدم هذا Lexaura؟

هذا الرسم يعطي Lexaura القدرة على:

- تقديم توصيات شخصية حسب طريقة الدراسة  
- اكتشاف الطلاب الذين يعانون في Online  
- اقتراح الانتقال إلى Hybrid أو Offline  
- تخصيص خطط دراسة حسب البيئة  
- تحليل تأثير Study_Method على Final Score بدقة

مثال توصية ذكية داخل Lexaura:

> “Your performance pattern suggests that you may benefit from more structured study environments.  
> Switching from Online to Hybrid could increase your expected score by 5–10 points.”

---
# DATA STORYTELLING (Pairplot of academic and psychological factors)

🚀 6. كيف يخدم هذا Lexaura؟

هذا الرسم هو الأساس لبناء نموذج توصيات ذكي متعدد العوامل داخل Lexaura:

- يمكن للنظام أن يتنبأ بالنتيجة بناءً على مزيج من الدراسة والقلق والضغط.  
- يمكنه تقديم توصيات شخصية مثل:  
  > “Your stress level is moderate, but your study hours are low. Increasing study time by 2 hours could raise your predicted score by 8 points.”  
- يمكنه اكتشاف الحالات النفسية التي تحتاج دعمًا إضافيًا.  
- يمكنه تحليل التفاعل بين العوامل النفسية والأكاديمية بشكل ديناميكي.

---
GRADE

5. Machine Learning Interpretation
For predictive modeling:

- Hours_Studied will be one of the top features in any Grade classification model  
- It provides strong separability between classes  
- It reduces model uncertainty  
- It improves interpretability and explainability  

This makes it ideal for explainable AI models.
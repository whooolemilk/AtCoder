# AtCoderあきらめないぞ
## lambda式

>基本
```python
名前 = lambda 引数, 引数, ...: 式
```

> 例文
```python:lambda
#def文
def add_def(a, b=1):
    return a + b

#lambda
add_lambda = lambda a, b=1: a + b

#実行結果
print(add_def(3, 4))
# 7

print(add_def(3))
# 4

print(add_lambda(3, 4))
# 7

print(add_lambda(3))
# 4
```

>lambda式でif文を使う
```python:lambda-if
get_odd_even = lambda x: 'even' if x % 2 == 0 else 'odd'

print(get_odd_even(3))
# odd

print(get_odd_even(4))
# even
```
>活用例   
>> sorted(), sort(), max(), min()の引数keyにlambda式
- リストをソートする組み込み関数sorted()やリストのメソッドsort()、最大値や最小値を返す組み込み関数max()やmin()には引数keyがある。

- keyには、ソートや最大値・最小値の算出の前に（各要素が比較される前に）リストの各要素に適用される関数を指定する。

- 通常ならsort()はアルファベット順だが、引数`key`を指定すると

```python:lambda-example
l = ['Charle', 'Bob', 'Alice']

l_sorted_len = sorted(l, key=len)

print(l_sorted_len)
# ['Bob', 'Alice', 'Charle']
```
- ここでさらにlambda式を使うと、任意の関数を各要素に適用してその結果を元にソートできる。
```python:lambda-sort
#2文字目を取得するラムダ式
print((lambda x: x[1])('Alice'))
# l

#引数keyに指定すると、2文字目のアルファベット順にソート
l_sorted_second = sorted(l, key=lambda x: x[1])

print(l_sorted_second)
# ['Charle', 'Alice', 'Bob']
```
>> map()やfilter()の第一引数にlambda式
- リストの各要素に対して関数を適用する組み込み関数map()や、条件を満たす要素のみ抽出する組み込み関数filter()では、第一引数に関数、第二引数にリストなどのイテラブルオブジェクトを指定する。

- 任意の関数を指定したい場合、def文で関数を定義するよりラムダ式で無名関数を指定したほうが簡潔に書ける。

>>>map関数
```python
l = [0, 1, 2, 3]

map_square = map(lambda x: x**2, l)

print(map_square)
# <map object at 0x1072fd128>

print(list(map_square))
# [0, 1, 4, 9]

#リスト内包表記のほうが簡潔
l_square = [x**2 for x in l]

print(l_square)
# [0, 1, 4, 9]

#イテレータを取得したい場合は、ジェネレータ式（ジェネレータ内包表記）
g_square = (x**2 for x in l)

print(g_square)
# <generator object <genexpr> at 0x1072b6d00>

print(list(g_square))
# [0, 1, 4, 9]
```


## 三項演算子
> 基本
```python
条件式が真のときに評価される式 if 条件式 else 条件式が偽のときに評価される式
```
```python
条件式が真のときに返す値 if 条件式 else 条件式が偽のときに返す値
```
> 例文
```python
# 条件によって処理を切り替えたい
a = 1
result = a * 2 if a % 2 == 0 else a * 3
print(result)
# 3

a = 2
result = a * 2 if a % 2 == 0 else a * 3
print(result)
# 4

# 条件によって値を切り替えたいとき
a = 1
result = 'even' if a % 2 == 0 else 'odd'
print(result)
# odd

a = 2
result = 'even' if a % 2 == 0 else 'odd'
print(result)
# even

#　値を返さない式（Noneを返す式）
a = 1
print('even') if a % 2 == 0 else print('odd')
# odd

```
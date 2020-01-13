"""
enumerate(): 返回可迭代对象的值和索引
zip(): 返回一个元组
zip(*): 解压, 返回二维矩阵式
"""

seq1 = ["jay", "sanford", "a"]
seq2 = ["chou", "luo", "b"]

for i, (a, b) in enumerate(zip(seq1, seq2)):
    print('{0}: {1}, {2}'.format(i, a, b))

pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'), ('Schilling', 'Curt')]
first_names, last_names = zip(*pitchers)

print(first_names, last_names)

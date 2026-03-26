def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):  
    return a / b
def mod(a, b):
    return a % b
exp =input()
if '+' in exp:
    a,b =exp.split('+')
    print(add(float(a),float(b)))
elif '-' in exp:
    a,b =exp.split('-')
    print(sub(float(a),float(b)))
elif '*' in exp:
    a,b =exp.split('*')
    print(mul(float(a),float(b)))
elif '/' in exp:
    a,b =exp.split('/')
    print(div(float(a),float(b)))
elif '%' in exp:
    a,b =exp.split('%')
    print(mod(float(a),float(b)))
main()

    


        
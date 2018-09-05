import re

def pig_it(input):
    words = input.split()
    output = []
    for w in words:
        p = ''
        if not w[-1].isalpha():
            p = w[-1]
            w = w[:-1]
        if w:
            output.append(w[1:] + w[0] + 'ay' + p)
        else:
            output.append(p)
    return ' '.join(output)

def pig_it2(input):
    words = re.findall(r"[\w']+|[.,!?; ]", input)
    output = [w[1:] + w[0] + 'ay' if w.isalpha() else w for w in words]
    return "".join(output)

print "ATTEMPT 1"
print pig_it('Pig latin is cool') # igPay atinlay siay oolcay
print pig_it('Hello world !')     # elloHay orldWay !
print pig_it('does this, work with commas') # oesday histay, orkway ithway ommascay

print "ATTEMPT 2"
print pig_it2('Pig latin is cool') # igPay atinlay siay oolcay
print pig_it2('Hello world !')     # elloHay orldWay !
print pig_it2('does this, work with commas') # oesday histay, orkway ithway ommascay

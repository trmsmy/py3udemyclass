str = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean tempus nibh quis ligula tristique, a venenatis 
nisl interdum. Donec nec augue ac tortor tempor fringilla. Maecenas odio nisi, ultrices a turpis ac, congue rutrum ex.
Vivamus vestibulum bibendum blandit. Maecenas faucibus, massa in feugiat facilisis, odio diam vehicula dolor, 
non porttitor tortor purus at ipsum. Duis elementum dapibus elit non tempus. Donec scelerisque urna sed mattis cursus.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc iaculis metus nisl. Morbi nisi nulla, 
aliquet quis accumsan non, mollis non nisi. Integer diam eros, faucibus ac lorem nec, rutrum ullamcorper urna.
Nullam ut hendrerit elit. Etiam sollicitudin eget nisl id venenatis. Nam vehicula erat at orci sagittis facilisis. 
Cras volutpat lobortis libero ut facilisis.
'''


print(str)

list = str.split(' ')

print("no. of words %d" % len(list))

set = { w for w in list }

print("no. of uniq words %d" % len(set))


#hash = { w: c for w in list}
hash = {}
for w in list:
    hash[w] = hash[w]+1 if w in hash else 1

print(hash)

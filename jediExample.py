import jedi
source = '''
import json
json.lo'''
script = jedi.Script(source, path='jediExample.py')
script
completions = script.complete(3, len('json.lo'))
completions
print(completions[0].complete)
print(completions[0].name)
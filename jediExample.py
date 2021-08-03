from jedi import Script

source = '''
import json
json.lo'''
script = Script(source)
print(f'script: {script}')
completions = script.complete(3, len('json.lo'))
print(f'completions: {completions}')
print(f'completions[0].complete: {completions[0].complete}')
print(f'completions[0].name: {completions[0].name}')

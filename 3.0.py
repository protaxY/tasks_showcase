import sys

query = None
filenames = []

for input_line in sys.stdin:
    input_line = input_line.strip()
    if not query:
        query = input_line.lower()
    else:
        filenames.append(input_line)
        
result = []

for filename in filenames:
    with open(filename, 'r') as f:
        content = f.read()
        content = content.lower()
        content = ' '.join(content.split())
        
        if query in content:
            result.append(filename)
    
if len(result):        
    for filename in result:
        print(filename)
else:
    print('404. Not Found')
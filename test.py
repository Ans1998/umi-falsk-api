arr = [{'name': '20191202160542.csv'}, {'name': '20191202160545.csv'}, {'name': '20191202160549.csv'}]
print(type(arr))
if (type(arr) == list):
    print('list')
else:
    print('else')
for fileItem in arr.items():
    print(fileItem)
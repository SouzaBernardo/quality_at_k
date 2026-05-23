```
To complete the class JSONProcessor, you need to implement the following methods:

1. read_json(file_path): This method should read a JSON file and return the data.
2. write_json(data, file_path): This method should write data to a JSON file and save it to the given path.
3. process_json(file_path, remove_key): This method should read a JSON file, remove the specified key from the JSON object, and rewrite the modified data back to the file.

Here is an example of how you can use the JSONProcessor class:

>>> json = JSONProcessor()
>>> json.read_json('test.json')
{'name': 'test', 'age': 14}
>>> json.write_json({'name': 'new_name', 'age': 15}, 'test.json')
1
>>> json.read_json('test.json')
{'name': 'new_name', 'age': 15}
>>> json.process_json('test.json', 'name')
1
>>> json.read_json('test.json')
{'age': 15}
```
Please make sure to follow the instructions and complete the class JSONProcessor as described.
```
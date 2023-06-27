# datakit

datakit is a python library for dealing with various real life data structures and its usage. Data Structures like stack , queue , heap , tree , graph , matrix , linked list , array have been implemented and ready to use. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install datakit.

```bash
pip install datakit
```

## Usage

```python
from datakit import stack
from datakit import queue
from datakit import linked_list
from datakit import node

# Initialize a stack 

st = stack(size=10)
st.insert(1)
st.pop()

qu = queue(size=10)
qu.insert(1)
qu.pop()

ll = linked_list()
nd = Node(1)
ll.head = nd



```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
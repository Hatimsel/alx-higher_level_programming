#include <Python.h>
#include <stdio.h>

/**
* print_python_list_info - prints infos concerning Python list.
*
* @p: a pointer to Python list object.
*/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	const char *item_type;
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
	item = PyList_GetItem(p, i);
	item_type = Py_TYPE(item)->tp_name;
	printf("Element %ld: %s\n", i, item_type);
	}
}

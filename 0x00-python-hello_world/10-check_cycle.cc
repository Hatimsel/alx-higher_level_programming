#include "lists.h"

/**
* check_cycle - function that checks is there is a cycle
*
* @list: linked list to be examined
*
* Return: returns 1 if there is a cycle else 0
*/


int check_cycle(listint_t *list)
{
	listint_t *arr[1024];
	int i = 0, j = 0;

	if (list == NULL)
	{
		return (0);
	}
	while (list != NULL)
	{
		arr[i] = list;
		list = list->next;
		while (arr[j] != NULL)
		{
			if (list == arr[j])
			{
				return (1);
			}
		j++;
		}
		i++;
	}
	return (0);
}

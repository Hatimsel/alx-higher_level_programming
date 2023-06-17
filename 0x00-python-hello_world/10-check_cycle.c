#include "lists.h"

/**
* check_cycle - function that checks is there is a cycle
*
* @list: linked list to be examined
* Return: returns 1 if there is a cycle else 0
*/

int check_cycle(listint_t *list)
{
	listint_t *tmp = list;

	if (list == NULL)
	{
		return (0);
	}
	while (list != NULL)
	{
		while (tmp != NULL)
		{
			if (tmp->next == list)
			{
				return (1);
			}
			tmp = tmp->next;
		}
		list = list->next;
	}
	return (0);
}

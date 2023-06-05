#include "lists.h"


int check_cycle(listint_t *list)
{
	listint_t *arr[1024];
	int i = 0, j = 0;

	if (list == NULL)
	{
		return (0);
	}
	while(list != NULL)
	{
		arr[i] = list;
		list = list->next;
		while(arr[j] != NULL)
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

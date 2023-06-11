#include "lists.h"

/**
* is_palindrome - checks if the singly linked list is a palindrome
* @head: pointer to pointer to the linked list's head
* Return: return 1 if it is palindrome else 0
*/

int is_palindrome(listint_t **head)
{
	int arr[MAX_LEN], i = 0, j = 0;
	listint_t *curr = *head;
	
	if (curr == NULL)
	{
	return (1);
	}
	else
	{
	while (curr != NULL)
	{
		arr[i] = curr->n;
		curr = curr->next;
		i++;
	}
	while (i > j)
	{
		if (arr[i - 1] != (*head)->n)
			return (0);
		else
		{
			(*head) = (*head)->next;
			i--;
			j++;
		}
	}
	}
	return (1);
}

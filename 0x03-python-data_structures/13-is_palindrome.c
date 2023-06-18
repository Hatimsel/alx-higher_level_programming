#include "lists.h"

/**
* is_palindrome - checks if the singly linked list is a palindrome
* @head: pointer to pointer to the linked list's head
* Return: return 1 if it is palindrome else 0
*/
#define max_len 100

int is_palindrome(listint_t **head)
{
	int arr[max_len];
	listint_t *curr = *head;
	int i = 0, j = 0, x = 0, len = 0, m_len = 0;
	if (*head == NULL)
	{
		return (1);
	}
	while (curr != NULL)
	{
		arr[i] = curr->n;
		i++;
		curr = curr->next;
	}
	arr[i] = '\0';
	while (arr[j] != '\0')
	{
		len++;
		j++;
	}
	if (len % 2 != 0)
	{
		return (1);
	}
	else
	{
		m_len = len / 2;
		for (x = 0; x < m_len; x++)
		{
			if (arr[len - 1] != arr[x])
			{
				return (0);
			}
			len--;
		}
		return (1);
	}
}

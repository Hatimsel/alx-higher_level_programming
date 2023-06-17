#include "lists.h"

/**
* insert_node -  inserts a number into a sorted singly linked list
* @head: pointer to pointer of first node of listint_t list
* @number: the data of the new node
* Return: returns the address of the new node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head, *tmp, *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		tmp = *head;
		*head = new_node;
		new_node->next = tmp->next;
		return (new_node);
	}
	while (curr->next != NULL && number > curr->next->n)
	{
		curr = curr->next;
	}
	new_node->next = curr->next;
	curr->next = new_node;

	return (new_node);
}

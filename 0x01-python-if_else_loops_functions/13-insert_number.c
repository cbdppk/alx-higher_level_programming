#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * insert_node - for inserting a node in a sorted list
 * @head: the head pointer
 * @number: the int data
 *
 * Return: returns 0
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr;
	listint_t *new_node;
	listint_t *prev;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	ptr = *head;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (ptr && ptr->n < number)
	{
		prev = ptr;
		ptr = ptr->next;
	}

	new_node->next = ptr;
	if (prev)
	{
		prev->next = new_node;
	}
	return (new_node);
}

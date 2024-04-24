#include <stdio.h>
#include <string.h>
#include "lists.h"

/**
 * check_cycle - for checking if there is a cycle in a list
 * @list: the head pointer
 * Return: returns 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}

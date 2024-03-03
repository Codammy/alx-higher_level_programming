#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks for a palindrome in a linked list
 * @list: linked list
 *
 * Return: 1 on Success
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list->next, *head = list;

	while (current)
	{
		while (list->next != current)
		{
			if (current->next == list)
				return (1);
			list = list->next;
		}
		current = current->next;
		list = head;
	}

	return (0);
}

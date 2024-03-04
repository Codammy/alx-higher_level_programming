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
	listint_t *curr = list, *head = list;

	while (curr)
	{
		while (list)
		{
			if (curr->next == list || curr->next == curr)
				return (1);
			if (curr == list)
				break;
			list = list->next;
		}
		curr = curr->next;
		list = head;
	}
	return (0);
}

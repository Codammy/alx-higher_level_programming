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
		if (curr->next == list)
			return (1);
		if (curr == list)
		{
			list = head;
			curr = curr->next;
			continue;
		}
		list = list->next;
	}
	return (0);
}

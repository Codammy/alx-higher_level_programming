#include "lists.h"

/**
 * check_cycle - checks for a palindrome in a linked list
 * @list: linked list
 *
 * Return: 1 on Success
 */
int check_cycle(listint_t *list)
{
	listint_t *start = list;

	while (list)
	{
		if (start == list->next)
			return (1);
		list = list->next;
	}

	return (0);
}

#include "lists.h"

/**
 * check_cycle - checks for a palindrome in a linked list
 * @list: linked list
 *
 * Return: 1 on Success
 */
int check_cycle(listint_t *list)
{
	listint_t *begin;

	while (list)
	{
		begin = list->next;
		while (begin)
		{
			if (begin == list)
				return (1);
			begin = begin->next;
		}
		list = list->next;
	}

	return (0);
}

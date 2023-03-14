#include "lists.h"

/**
 * check_cycle - checks if a node links to its head
 * @list: linked list
 * Return: 0 | 1
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	tmp = list;
	while (list != NULL)
	{
		list = (*list).next;
		if (list == tmp)
			return (1);
	}
	return (0);
}

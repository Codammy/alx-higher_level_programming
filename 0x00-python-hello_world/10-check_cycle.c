#include "lists.h"

/**
 * check_cycle - checks if a node links to its head
 * @list: linked list
 * Return: 0 | 1
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;
	listint_t *rn;

	tmp = list;
	while (list != NULL)
	{
	//	tmp = list->next;
		while (tmp != NULL)
		{
			if (tmp == list)
				return (1);
			tmp = tmp->next;
		}
		list = list->next;
	}
	return (0);
}

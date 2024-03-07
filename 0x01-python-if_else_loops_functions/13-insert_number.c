#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to node
 * @number: number to add
 *
 * Return: address of new node on success.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp, *curr;

	if (!head)
		return (NULL);
	new = malloc(sizeof(*head));
	new->n = number;
	new->next = NULL;

	if (!(*head))
	{
		*head = new;
		return (new);
	}
	else
	{
		curr = *head;
		tmp = curr->next;
		while (curr)
		{
			if (number < curr->n)
			{
				new->next = curr;
				*head = new;
				break;
			}
			else if ((number >= curr->n) && (!tmp || number < tmp->n))
			{
				new->next = curr->next;
				curr->next = new;
				break;
			}
			curr = curr->next;
			tmp = tmp->next;
		}
	}
	return (new);
}

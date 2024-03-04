#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks for a cycle in a linked list
 * @list: linked list
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
    listint_t *tortoise = list, *hare = list;

    while (hare && hare->next)
    {
        tortoise = tortoise->next;
        hare = hare->next->next;

        if (tortoise == hare)
            return (1);
    }

    return (0);
}

#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 * Return: 0 if no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *predator, *prey;
	
	if (list == NULL || list->next == NULL)
		return (0);
	predator = list->next;
	prey = list->next->next;
	while (predator && prey && prey->next)
	{
		if (predator == prey)
			return (1);
		predator = predator->next;
		prey = prey->next->next;
	}
	return (0);
}

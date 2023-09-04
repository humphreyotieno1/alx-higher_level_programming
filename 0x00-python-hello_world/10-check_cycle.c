#include "lists.h"

/**
 * check_cycle - check if linked list has a cycle
 * @list: list checked
 * Return: 1 if list as cycle, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *low = list;
	listint_t *high = list;

	if (!list)
		return (0);

	while (low && high && high->next)
	{
		low = high->next;
		high = high->next->next;
		if (low == high)
			return (-1);
	}
	return (0);
}

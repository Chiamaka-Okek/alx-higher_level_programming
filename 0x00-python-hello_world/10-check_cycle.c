#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it              
*
* @list: pointer to node
*
* Return: 0 if there is no cycle otherwise return 1 if cycle exists
*/
int check_cycle(listint_t *list)
{
	listint_t *a;
	listint_t *b;

	a = b = list;
	while (list != NULL)
	{
		a = a->next;
		b = b->next->next;
		if (!a || !b)
			return (0);
		if (b->next == a)
			return (1);
	}
	return (0);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tetrino_utils1.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <etexier@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/01/28 15:25:13 by etexier           #+#    #+#             */
/*   Updated: 2020/02/05 07:51:58 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "fillit.h"

int				is_on(t_ushort tetrino, int index)
{
	if (((tetrino >> (15 - index)) & 0x0001) == 1)
		return (1);
	return (0);
}

t_tetrino		*add_to_list(t_tetrino **first, t_tetrino *new)
{
	t_tetrino *tmp;

	tmp = *first;
	while (tmp)
	{
		if (tmp->next == NULL)
		{
			tmp->next = new;
			return (*first);
		}
		tmp = tmp->next;
	}
	*first = new;
	return (*first);
}

static int		get_xspan(unsigned char val, int pos)
{
	if (pos == 3)
		return (1);
	if (pos == 2)
	{
		if (val == 3)
			return (2);
		return (1);
	}
	if (pos == 1)
	{
		if ((val & 0x1) == 1)
			return (3);
		if ((val & 0x2) == 2)
			return (2);
		return (1);
	}
	if ((val & 0x1) == 1)
		return (4);
	if ((val & 0x2) == 2)
		return (3);
	if ((val & 0x4) == 4)
		return (2);
	return (1);
}

static void		span_x(t_tetrino *t, int line, int *start, int *span)
{
	static int				shift[4] = {12, 8, 4, 0};
	unsigned char			val;

	val = (unsigned char)((t->shape >> shift[line]) & 0xF);
	*start = -1;
	*span = 0;
	if (val > 7)
		*start = 0;
	else if (val > 3)
		*start = 1;
	else if (val > 1)
		*start = 2;
	else if (val == 1)
		*start = 3;
	if (*start != -1)
		*span = get_xspan(val, *start);
}

void			do_span(t_tetrino *t)
{
	int start;
	int span;
	int line;

	line = 0;
	while (line < 4)
	{
		span_x(t, line, &start, &span);
		t->spanx[line].start = start;
		t->spanx[line].span = span;
		line++;
	}
	return ;
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tetrino_utils.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <etexier@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/01/27 20:42:12 by eric              #+#    #+#             */
/*   Updated: 2020/02/07 11:40:33 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "fillit.h"

static t_tetrino	*alloc_s_tetrino(t_ushort shape)
{
	t_tetrino	*ptr;

	ptr = (t_tetrino *)malloc(sizeof(t_tetrino));
	if (ptr == NULL)
		return (NULL);
	ptr->shape = shape;
	ptr->next = NULL;
	bound(shape, ptr->box, ptr->box + 1);
	do_span(ptr);
	return (ptr);
}

t_tetrino			*make_s_tetrino(t_ushort t)
{
	int index;
	int count;

	index = 0;
	count = 0;
	while (count < 16)
	{
		if (is_on(t, count) == 1)
		{
			if (index >= 4)
				return (0);
			index++;
		}
		count++;
	}
	if (index != 4)
		return (NULL);
	count = is_valid_shape(t);
	if (count == -1)
		return (NULL);
	return (alloc_s_tetrino(t));
}

static t_ushort		shift_left(t_ushort tetrino)
{
	char	l1;
	char	l2;
	char	l3;
	char	l4;

	l1 = ((tetrino >> 12) << 1) & 0x000F;
	l2 = ((tetrino >> 8) << 1) & 0x000F;
	l3 = ((tetrino >> 4) << 1) & 0x000F;
	l4 = ((tetrino << 1) & 0x000F);
	tetrino = (l1 << 12) + (l2 << 8) + (l3 << 4) + l4;
	return (tetrino);
}

t_ushort			move_to_top(t_ushort tetrino)
{
	int		count;

	count = 0;
	while (count < 3)
	{
		if ((tetrino & 0xF000) == 0)
			tetrino = tetrino << 4;
		count++;
	}
	count = 0;
	while (count < 3)
	{
		if (is_on(tetrino, 0) == 0 && is_on(tetrino, 4) == 0 &&
			is_on(tetrino, 8) == 0 && is_on(tetrino, 12) == 0)
			tetrino = shift_left(tetrino);
		count++;
	}
	return (tetrino);
}

void				delete_list_tetrino(t_tetrino **lst)
{
	t_tetrino	*tmp;
	t_tetrino	*next;

	tmp = *lst;
	while (tmp)
	{
		next = tmp->next;
		free(tmp);
		tmp = next;
	}
	*lst = NULL;
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tetrino_utils2.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <etexier@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/01/28 15:27:49 by etexier           #+#    #+#             */
/*   Updated: 2020/02/05 07:51:51 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "fillit.h"

static t_ushort		*get_objects_local(void)
{
	static t_ushort	shape_object[SHAPES_MAX] = {0xf000,
												0xe200,
												0xe400,
												0xe800,
												0xcc00,
												0xc600,
												0xc440,
												0xc880,
												0x8E00,
												0x8c80,
												0x8c40,
												0x88c0,
												0x8888,
												0x6c00,
												0x4E00,
												0x4C80,
												0x44C0,
												0x4C40,
												0x2E00};

	return (shape_object);
}

static t_ushort		get_single_row_val(char *a_row)
{
	int			count;
	short int	res;

	res = 0;
	count = 0;
	while (count < 4)
	{
		if (a_row[count] == SHAPE)
			res = (res << 1) + 1;
		else if (a_row[count] == EMPTY)
			res = (res << 1);
		else
			return (0);
		count++;
	}
	return (res);
}

static t_ushort		add_tetrino_line(t_ushort val, char *a_row)
{
	return ((val << 4) + get_single_row_val(a_row));
}

int					is_valid_shape(t_ushort t)
{
	int					count;
	t_ushort			*def;

	count = 0;
	def = get_objects_local();
	while (count < SHAPES_MAX)
	{
		if (t == def[count])
			return (count);
		count++;
	}
	return (-1);
}

t_ushort			make_tetrino(char *row1,
								char *row2,
								char *row3,
								char *row4)
{
	int		c;

	c = -1;
	while (c++ < 3)
	{
		if (row1[c] != SHAPE && row1[c] != EMPTY)
			return (0);
	}
	c = -1;
	while (c++ < 3)
		if (row2[c] != SHAPE && row2[c] != EMPTY)
			return (0);
	c = -1;
	while (c++ < 3)
		if (row3[c] != SHAPE && row3[c] != EMPTY)
			return (0);
	c = -1;
	while (c++ < 3)
		if (row4[c] != SHAPE && row4[c] != EMPTY)
			return (0);
	return (add_tetrino_line(
			add_tetrino_line(
			add_tetrino_line(
			add_tetrino_line(0, row1), row2), row3), row4));
}

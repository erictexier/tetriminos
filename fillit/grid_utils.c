/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   grid_utils.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <etexier@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/01/06 10:01:11 by etexier           #+#    #+#             */
/*   Updated: 2020/02/07 11:45:39 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "fillit.h"
#include "libft/libft.h"

static void		init_off(t_tetrino *t, t_grid *grid)
{
	t->cd[ROW] = 0;
	t->cd[COL] = 0;
	t->max_box[ROW] = grid->csize - t->box[COL] + 1;
	t->max_box[COL] = grid->csize - t->box[ROW] + 1;
}

void			init_offset(t_tetrino *t, t_grid *grid)
{
	int		start;
	int		count;
	int		offset;
	int		end;
	int		point;

	count = 0;
	point = 0;
	offset = 0;
	while (count < 4 && t->spanx[count].start != -1)
	{
		start = t->spanx[count].start;
		end = start + t->spanx[count].span;
		while (start < end)
		{
			t->offset[point] = offset + start;
			point++;
			start++;
		}
		offset += grid->csize;
		count++;
	}
	init_off(t, grid);
}

int				resize_iter(t_grid *grid)
{
	t_tetrino	*t;

	if (grid->csize + 1 < GRID_SIZE_MAX)
	{
		grid->csize++;
		grid->sq_size = grid->csize * grid->csize;
		ft_memset(&grid->table2, EMPTY, grid->sq_size);
		t = grid->tetrino_input;
		while (t != NULL)
		{
			init_offset(t, grid);
			t = t->next;
		}
		return (1);
	}
	return (0);
}

int				display_result2(t_grid *grid)
{
	int		row;
	int		col;
	char	*ptr;

	row = 0;
	ptr = grid->table2;
	while (row < grid->csize)
	{
		col = 0;
		while (col < grid->csize)
		{
			ft_putchar(*ptr++);
			col++;
		}
		ft_putchar('\n');
		row++;
	}
	return (1);
}

int				get_csize(t_grid *grid)
{
	int			count;
	int			res;
	t_tetrino	*data;

	data = grid->tetrino_input;
	count = 0;
	while (data)
	{
		data = data->next;
		count++;
	}
	grid->nb_tetrino = count;
	res = 1;
	while ((res * res) < (count * 4))
		res++;
	return (res);
}

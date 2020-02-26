/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   resolve_iter.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <etexier@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/01/28 16:20:20 by etexier           #+#    #+#             */
/*   Updated: 2020/02/05 07:50:22 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft/libft.h"
#include "fillit.h"

static int		write_tetrino(char *ptr, t_tetrino *t, int row, int col)
{
	*(ptr + t->offset[0]) = t->marker;
	*(ptr + t->offset[1]) = t->marker;
	*(ptr + t->offset[2]) = t->marker;
	*(ptr + t->offset[3]) = t->marker;
	t->cd[0] = row;
	t->cd[1] = col;
	t->ptr = ptr;
	return (1);
}

static int		try_insert_tetrino2(t_grid *grid, t_tetrino *t)
{
	int		row;
	int		col;
	char	*ptr;

	row = t->cd[ROW];
	col = t->cd[COL];
	while (row < t->max_box[ROW])
	{
		ptr = grid->table2 + (row * grid->csize) + col;
		while (col < t->max_box[COL])
		{
			if (*(ptr + t->offset[0]) == EMPTY &&
				*(ptr + t->offset[1]) == EMPTY &&
				*(ptr + t->offset[2]) == EMPTY &&
				*(ptr + t->offset[3]) == EMPTY)
				return (write_tetrino(ptr, t, row, col));
			ptr++;
			col++;
		}
		col = 0;
		row++;
	}
	return (0);
}

static int		update_coord_iter(t_tetrino *t)
{
	if (t->cd[COL] + 1 < t->max_box[COL])
	{
		t->cd[COL] = t->cd[COL] + 1;
		return (1);
	}
	t->cd[COL] = 0;
	if (t->cd[ROW] + 1 < t->max_box[ROW])
	{
		t->cd[ROW] = t->cd[ROW] + 1;
		return (1);
	}
	return (0);
}

static int		resolve_rec2(t_grid *grid, t_tetrino *t)
{
	int		res;
	char	*ptr;

	if (try_insert_tetrino2(grid, t) == 0)
		return (0);
	if (t->next == NULL)
		return (1);
	t->next->cd[ROW] = 0;
	t->next->cd[COL] = 0;
	res = resolve_rec2(grid, t->next);
	if (res == 0)
	{
		ptr = t->ptr;
		*(ptr + t->offset[0]) = EMPTY;
		*(ptr + t->offset[1]) = EMPTY;
		*(ptr + t->offset[2]) = EMPTY;
		*(ptr + t->offset[3]) = EMPTY;
		if (update_coord_iter(t) == 0)
			return (0);
		return (resolve_rec2(grid, t));
	}
	return (1);
}

int				resolve_iter2(t_grid *grid)
{
	t_tetrino	*t;

	ft_memset(&grid->table2, EMPTY, grid->sq_size);
	t = grid->tetrino_input;
	t->cd[0] = 0;
	t->cd[1] = 0;
	while (resolve_rec2(grid, t) == 0)
	{
		if (resize_iter(grid) == 0)
			return (0);
	}
	return (1);
}

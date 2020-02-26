/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   grid_utils2.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <etexier@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/02/07 11:44:29 by etexier           #+#    #+#             */
/*   Updated: 2020/02/07 11:45:25 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "fillit.h"
#include "libft/libft.h"

t_grid			*init_grid(t_tetrino *lst)
{
	t_grid		*grid;
	int			marker;

	marker = 65;
	grid = (t_grid *)malloc(sizeof(t_grid));
	if (grid == NULL)
		return (NULL);
	grid->tetrino_input = lst;
	grid->csize = get_csize(grid);
	grid->sq_size = grid->csize * grid->csize;
	while (lst)
	{
		if (marker > 'Z')
		{
			free(grid);
			return (NULL);
		}
		lst->marker = marker;
		marker++;
		init_offset(lst, grid);
		lst = lst->next;
	}
	return (grid);
}

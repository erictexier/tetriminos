/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fillit.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <etexier@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/21 13:52:23 by etexier           #+#    #+#             */
/*   Updated: 2020/02/07 11:37:19 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft/libft.h"
#include "fillit.h"
#include "get_next_line.h"

static int		add_tetrino(t_tetrino **ll, char *b[4])
{
	t_ushort			val;
	t_tetrino			*t;

	val = make_tetrino(b[0], b[1], b[2], b[3]);
	free(b[0]);
	free(b[1]);
	free(b[2]);
	free(b[3]);
	val = move_to_top(val);
	t = make_s_tetrino(val);
	if (t)
	{
		*ll = add_to_list(ll, t);
		return (1);
	}
	delete_list_tetrino(ll);
	return (0);
}

static int		check_buf(int *cl, int *ce, char *b[4], char *line)
{
	if (ft_strlen(line) == 4)
	{
		if (*ce == -1)
			return (0);
		*ce = 0;
		if (*cl < 4)
			b[*cl] = ft_strdup(line);
		(*cl)++;
	}
	else if (ft_strlen(line) == 0)
	{
		if (*ce == -1)
			*ce = 0;
		(*cl) = 0;
		(*ce)++;
	}
	else
		return (0);
	return (1);
}

static int		is_valid(int *cl, int *ce, char *b[4], t_tetrino **lst)
{
	if (*cl == 4)
	{
		if (!add_tetrino(lst, b))
		{
			delete_list_tetrino(lst);
			return (0);
		}
		*cl = 0;
		*ce = -1;
	}
	if (*ce > 1)
	{
		delete_list_tetrino(lst);
		return (0);
	}
	return (1);
}

t_tetrino		*ft_fillit_reader(int fd)
{
	char		*line;
	char		*b[4];
	int			count_line;
	int			count_empty;
	t_tetrino	*lst_ttx;

	line = NULL;
	count_line = 0;
	count_empty = 0;
	lst_ttx = NULL;
	while (get_next_line(fd, &line) == 1)
	{
		if (check_buf(&count_line, &count_empty, b, line) == 0)
			return (NULL);
		if (!is_valid(&count_line, &count_empty, b, &lst_ttx))
			return (NULL);
		free(line);
	}
	if (count_line != 0)
	{
		delete_list_tetrino(&lst_ttx);
		return (NULL);
	}
	return (lst_ttx);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <etexier@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/01/06 17:03:34 by etexier           #+#    #+#             */
/*   Updated: 2020/02/07 11:40:51 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include "fillit.h"
#include "libft/libft.h"

static int		go(t_tetrino *lst_ttx)
{
	t_grid		*grid;

	grid = init_grid(lst_ttx);
	if (grid == NULL)
		return (0);
	if (resolve_iter2(grid))
		display_result2(grid);
	free(grid);
	delete_list_tetrino(&lst_ttx);
	return (1);
}

int				main(int argc, char **argv)
{
	int			fd;
	t_tetrino	*lst_ttx;

	if (argc != 2)
	{
		write(1, USAGE, sizeof(USAGE));
		return (0);
	}
	fd = open(argv[1], O_RDONLY);
	if (fd == -1)
	{
		write(1, USAGE, sizeof(USAGE));
		return (0);
	}
	lst_ttx = ft_fillit_reader(fd);
	if (lst_ttx == NULL)
	{
		write(1, FILE_NOT_FORMAT, sizeof(FILE_NOT_FORMAT));
		return (0);
	}
	return (go(lst_ttx));
}

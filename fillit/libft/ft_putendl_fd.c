/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putendl_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/11 16:52:32 by etexier           #+#    #+#             */
/*   Updated: 2019/11/14 13:18:54 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include "libft.h"

void	ft_putendl_fd(char const *s, int fd)
{
	char c;

	if (s == NULL)
		return ;
	while (*s)
	{
		c = *s;
		write(fd, &c, 1);
		s++;
	}
	write(fd, "\n", 1);
}

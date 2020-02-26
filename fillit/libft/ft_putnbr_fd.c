/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/11 16:54:44 by etexier           #+#    #+#             */
/*   Updated: 2019/11/15 18:21:20 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static void		rec_putnb_fd(long nb, int fd)
{
	long x;
	long div;

	if (nb <= 0)
		return ;
	div = 10;
	x = nb % div;
	nb = nb / div;
	rec_putnb_fd(nb, fd);
	ft_putchar_fd(x + 48, fd);
}

void			ft_putnbr_fd(int nb, int fd)
{
	long	ux;

	if (nb < 0)
	{
		ft_putchar_fd('-', fd);
		ux = (long)nb;
		ux = -ux;
	}
	else
	{
		ux = (long)nb;
	}
	if (nb == 0)
		ft_putchar_fd('0', fd);
	else
		rec_putnb_fd(ux, fd);
}

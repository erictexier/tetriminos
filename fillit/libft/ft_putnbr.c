/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/09/05 12:04:42 by etexier           #+#    #+#             */
/*   Updated: 2019/11/15 18:20:24 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static void		rec_putnb(long nb)
{
	long x;
	long div;

	if (nb <= 0)
		return ;
	div = 10;
	x = nb % div;
	nb = nb / div;
	rec_putnb(nb);
	ft_putchar(x + 48);
}

void			ft_putnbr(int nb)
{
	long	ux;

	if (nb < 0)
	{
		ft_putchar('-');
		ux = (long)nb;
		ux = -ux;
	}
	else
	{
		ux = (long)nb;
	}
	if (nb == 0)
		ft_putchar('0');
	else
		rec_putnb(ux);
}

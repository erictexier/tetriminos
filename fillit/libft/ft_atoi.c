/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/07 09:51:12 by etexier           #+#    #+#             */
/*   Updated: 2019/11/14 10:24:41 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	do_math(const char *str, int is_neg)
{
	double val;

	val = 0.;
	while (*str >= 48 && *str <= 57)
	{
		val = (val * 10) + (*str - 48);
		if (is_neg && val > MAX_LONGLONG)
			return (0);
		else if (val > MAX_LONGLONG)
			return (-1);
		str++;
	}
	if (is_neg)
		return (int)(long)(-val);
	return (int)(long)(val);
}

int			ft_atoi(const char *str)
{
	int		countneg;
	long	total;

	total = 0;
	countneg = 0;
	while (*str == 32 || (*str >= 9 && *str <= 13))
		str++;
	while (*str == '+' || *str == '-')
	{
		if (*str == '-')
			countneg++;
		total++;
		str++;
	}
	if (total > 1)
		return (0);
	return (do_math(str, countneg % 2));
}

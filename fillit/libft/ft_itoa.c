/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/11 14:50:30 by etexier           #+#    #+#             */
/*   Updated: 2019/11/15 18:54:34 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

static unsigned int		get_nb_of_digits(unsigned int nb)
{
	unsigned int count;

	count = 0;
	while (nb > 0)
	{
		count++;
		nb = nb / 10;
	}
	return (count);
}

static void				write_to_string(char *m, int unsigned nb, size_t size)
{
	if (size == 0)
		return ;
	m[size - 1] = (nb % 10) + 48;
	write_to_string(m, nb / 10, size - 1);
}

static char				*do_work(char *m, unsigned int nb, int n, size_t size)
{
	char			*ptr;

	ptr = m;
	if (n < 0)
	{
		*ptr = '-';
		ptr++;
		size--;
	}
	write_to_string(ptr, nb, size);
	return (m);
}

char					*ft_itoa(int n)
{
	size_t			size;
	unsigned int	nb;
	char			*m;

	if (n == 0)
	{
		m = (char *)malloc(sizeof(char) * (2));
		m[0] = 48;
		m[1] = '\0';
		return (m);
	}
	if (n < 0)
		nb = -n;
	else
		nb = n;
	size = get_nb_of_digits(nb);
	if (n < 0)
		size++;
	m = (char *)malloc(sizeof(char) * (size + 1));
	if (m == NULL)
		return (m);
	m[size] = '\0';
	return (do_work(m, nb, n, size));
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/07 13:03:53 by etexier           #+#    #+#             */
/*   Updated: 2019/11/14 10:33:49 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	unsigned char	*uc_src;
	unsigned char	stop;

	stop = (unsigned char)c;
	uc_src = (unsigned char *)s;
	while (n > 0)
	{
		if (*uc_src == stop)
			return (void *)(uc_src);
		if (*uc_src == 0)
			return (NULL);
		uc_src++;
		n--;
	}
	return (NULL);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/06 18:37:46 by etexier           #+#    #+#             */
/*   Updated: 2019/11/12 18:46:34 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dst, const void *src, size_t len)
{
	char		*c_src;
	char		*c_dst;
	size_t		count;

	count = -1;
	c_src = (char *)src;
	c_dst = (char *)dst;
	if (c_src < c_dst)
	{
		while ((int)(--len) >= 0)
		{
			*(c_dst + len) = *(c_src + len);
		}
	}
	else
	{
		while (++count < len)
		{
			*(c_dst + count) = *(c_src + count);
		}
	}
	return (dst);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/07 10:52:55 by etexier           #+#    #+#             */
/*   Updated: 2019/11/18 09:14:51 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t			ft_strlcat(char *dest, const char *src, size_t size)
{
	size_t	dstlen;
	size_t	srclen;

	srclen = ft_strlen(src);
	dstlen = ft_strlen(dest);
	if (size < dstlen)
		dstlen = size;
	if (dstlen == size)
		return (size + srclen);
	if (srclen < size - dstlen)
	{
		ft_memcpy(dest + dstlen, src, srclen + 1);
	}
	else
	{
		ft_memcpy(dest + dstlen, src, size - dstlen);
		*(dest + size - 1) = 0;
	}
	return (srclen + dstlen);
}

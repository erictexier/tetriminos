/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memccpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/06 14:23:54 by etexier           #+#    #+#             */
/*   Updated: 2019/11/15 13:57:50 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memccpy(void *dst, const void *src, int c, size_t n)
{
	unsigned char		*uc_dst;
	const unsigned char	*uc_src;

	uc_src = (unsigned char *)src;
	uc_dst = (unsigned char *)dst;
	if (n)
	{
		while (n != 0)
		{
			if ((*uc_dst++ = *uc_src++) == (unsigned char)c)
				return (void *)(uc_dst);
			n--;
		}
	}
	return (NULL);
}

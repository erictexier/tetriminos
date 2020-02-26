/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/07 11:52:16 by etexier           #+#    #+#             */
/*   Updated: 2019/11/11 19:49:41 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strncpy(char *dest, const char *src, size_t n)
{
	size_t	count;
	char	*dest_save;

	dest_save = dest;
	count = 0;
	while (*src && count < n)
	{
		*dest++ = *src++;
		count++;
	}
	while (count < n)
	{
		*dest++ = '\0';
		count++;
	}
	return (dest_save);
}

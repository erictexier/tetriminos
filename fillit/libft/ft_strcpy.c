/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/07 10:58:13 by etexier           #+#    #+#             */
/*   Updated: 2019/11/08 16:58:14 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strcpy(char *dest, const char *src)
{
	int		count;
	char	*dst_save;

	count = 0;
	dst_save = dest;
	while (*src)
	{
		*dest++ = *src++;
		count++;
	}
	if (count == 0)
	{
		*dest = '\0';
	}
	else
	{
		*dest = *src;
	}
	return (dst_save);
}

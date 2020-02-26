/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/07 14:22:38 by etexier           #+#    #+#             */
/*   Updated: 2019/11/11 19:49:54 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strchr(const char *s, int c)
{
	char val;

	val = (char)c;
	while (*s != '\0')
	{
		if (*s == val)
			return (char *)(s);
		s++;
	}
	if (val == *s)
		return (char *)(s);
	return (NULL);
}

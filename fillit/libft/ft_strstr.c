/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/07 10:42:47 by etexier           #+#    #+#             */
/*   Updated: 2019/11/14 14:56:16 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strstr(const char *str, const char *to_find)
{
	int len_needle;

	len_needle = ft_strlen(to_find);
	if (len_needle == 0)
		return ((char *)str);
	if (*str == '\0')
		return (char*)(NULL);
	while (*str)
	{
		if (ft_strncmp(str, to_find, len_needle) == 0)
			return (char*)(str);
		str++;
	}
	return ((char *)(NULL));
}

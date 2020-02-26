/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/15 13:39:29 by etexier           #+#    #+#             */
/*   Updated: 2019/11/15 13:54:24 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *str, const char *to_find, size_t len)
{
	size_t		len_find;
	size_t		current_len;
	char		*ptr_str;

	ptr_str = (char *)str;
	len_find = ft_strlen(to_find);
	if (len_find == 0)
		return ((char *)str);
	current_len = 0;
	while (*ptr_str)
	{
		if (current_len + len_find > len)
			return ((char*)NULL);
		if (ft_strncmp(ptr_str, to_find, len_find) == 0)
			return (char *)(ptr_str);
		ptr_str++;
		current_len++;
	}
	return ((char *)NULL);
}

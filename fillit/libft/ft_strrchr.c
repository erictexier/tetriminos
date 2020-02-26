/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/07 14:27:53 by etexier           #+#    #+#             */
/*   Updated: 2019/11/14 14:01:48 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	const char *res;
	const char *ptr;

	c = (unsigned char)c;
	if (c == '\0')
		return (ft_strchr(s, '\0'));
	res = NULL;
	while ((ptr = ft_strchr(s, c)) != NULL)
	{
		res = ptr;
		s = ptr + 1;
	}
	return (char *)res;
}

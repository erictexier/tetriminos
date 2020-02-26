/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/06 11:41:40 by etexier           #+#    #+#             */
/*   Updated: 2019/11/11 19:50:24 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

char	*ft_strdup(const char *src)
{
	int			count;
	const char	*s;
	char		*res;
	char		*m;

	s = src;
	count = 0;
	while (*s++)
		count++;
	count++;
	m = (char *)malloc(sizeof(char) * count);
	if (m == NULL)
		return (m);
	res = m;
	s = src;
	while (*s != '\0')
		*m++ = *s++;
	*m = '\0';
	return (res);
}

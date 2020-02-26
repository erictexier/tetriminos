/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strsub.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/08 17:44:16 by etexier           #+#    #+#             */
/*   Updated: 2019/11/18 14:49:40 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

char	*ft_strsub(char const *s, unsigned int start, size_t len)
{
	char			*m;
	char			*ptr;
	char			*ptr_src;
	size_t			size;

	if (s == NULL)
		return (NULL);
	size = ft_strlen(s);
	if (start + len > size)
		return (NULL);
	m = (char *)malloc((len + 1) * sizeof(char));
	if (m == NULL)
		return (NULL);
	ptr = m;
	ptr_src = (char *)s + start;
	while (len--)
		*ptr++ = *ptr_src++;
	*ptr = '\0';
	return (m);
}

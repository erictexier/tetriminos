/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/09/11 11:32:22 by etexier           #+#    #+#             */
/*   Updated: 2019/11/18 13:13:44 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

static char		*build_string(char *ptr,
						char const *s1, char const *s2, int l1)
{
	char *m;

	m = ptr;
	if (s1 != NULL)
		ft_strncpy(ptr, s1, l1);
	if (s2 != NULL)
	{
		ptr = ptr + l1;
		while (*s2)
			*ptr++ = *s2++;
	}
	*ptr = '\0';
	return (m);
}

char			*ft_strjoin(char const *s1, char const *s2)
{
	size_t		len_s1;
	size_t		len_s2;
	char		*m;

	if (s1 != NULL)
		len_s1 = ft_strlen(s1);
	else
		len_s1 = 0;
	if (s2 != NULL)
		len_s2 = ft_strlen(s2);
	else
		len_s2 = 0;
	m = (char *)malloc((len_s1 + len_s2 + 1) * sizeof(char));
	if (m == NULL)
		return (m);
	return (build_string(m, s1, s2, len_s1));
}

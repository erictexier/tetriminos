/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/08 17:26:01 by etexier           #+#    #+#             */
/*   Updated: 2019/11/18 09:54:00 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

static char		*my_empty_case(void)
{
	char	*res;

	res = (char *)malloc(1);
	if (res == 0)
		return (char *)(NULL);
	*res = '\0';
	return (res);
}

char			*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	char			*res;
	char			*ptr_res;
	size_t			size;
	unsigned int	index;

	index = 0;
	if (s == NULL)
		return (NULL);
	size = ft_strlen(s);
	if (size == 0)
		return ((char *)my_empty_case());
	res = (char *)malloc((size + 1) * sizeof(char));
	if (res == NULL)
		return (NULL);
	ptr_res = res;
	while (*s)
	{
		*res++ = f(index, *s);
		index++;
		s++;
	}
	*res = '\0';
	return (char *)(ptr_res);
}
